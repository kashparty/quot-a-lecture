from posixpath import split
from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.template import loader
from sentence_transformers import SentenceTransformer
from scipy.spatial import distance
from numpy import argsort, frombuffer, single
from django.db.models import F
import re
from os import listdir
import pickle
import nltk
from nltk.stem import WordNetLemmatizer
from datetime import datetime

from .models import Category, Lecturer, QuestionAnswer, Recording


model = SentenceTransformer("distilbert-base-nli-mean-tokens")
nltk.download("wordnet")
nltk.download("omw-1.4")
lemmatizer = WordNetLemmatizer()

# Question, preamble, answer
COEFFS = [75, 25, 25]

# Create your views here.


def index(req):
    ls = Recording.objects.order_by("-date")
    return render(req, "seapanapp/l_list.html", {"ls": ls})


def q_details(req, question_id):
    q = get_object_or_404(QuestionAnswer, pk=question_id)
    return render(req, "seapanapp/q_detail.html", {"q": q})


def q_upvote(req, question_id):
    QuestionAnswer.objects.filter(pk=question_id).update(votes=F("votes") + 1)
    return redirect("seapanapp:q_detail", question_id=question_id)


def q_downvote(req, question_id):
    QuestionAnswer.objects.filter(pk=question_id).update(votes=F("votes") - 1)
    return redirect("seapanapp:q_detail", question_id=question_id)


def lecture_detail(req, lecture_id):
    l = get_object_or_404(Recording, pk=lecture_id)
    qs = l.questions.order_by("timestamp")
    return render(req, "seapanapp/l_detail.html", {"l": l, "qs": qs})


def search(req):
    ls = Lecturer.objects.order_by("name")
    cs = Category.objects.order_by("name")
    return render(req, "seapanapp/search.html", {"ls": ls, "cs": cs})


def precalc_counts():
    counts = dict()
    files_dir = "panopto-api-stuff/"
    filenames = [f for f in listdir(files_dir) if f.endswith(".txt")]
    for filename in filenames:
        file = open(files_dir + filename, "r")
        for word in map(
            lambda w: lemmatizer.lemmatize(w),
            filter(
                lambda c: c != "",
                re.sub("[\n,.;@#?!&$]+", " ", file.read().lower()).split(" "),
            ),
        ):
            if word in counts:
                counts[word] += 1
            else:
                counts[word] = 1
    return counts


def save_counts():
    file = open("PrecalculatedCounts.dat", "wb")
    pickle.dump(precalc_counts(), file)
    file.close()


def load_counts():
    file = open("PrecalculatedCounts.dat", "rb")
    counts = pickle.load(file)
    file.close()
    return counts


counts = load_counts()


def heuristic(question1, question2):
    value = 0
    lem_question1 = split_to_words(question1)
    for i in range(len(lem_question1)):
        lem_question1[i] = lemmatizer.lemmatize(lem_question1[i])
    lem_question2 = split_to_words(question2)
    for i in range(len(lem_question2)):
        lem_question2[i] = lemmatizer.lemmatize(lem_question2[i])

    for word in lem_question1:
        if word in lem_question2 and word in counts:
            value += 1 / counts[word]

    return value


def split_to_words(inp):
    return list(
        filter(lambda c: c != "", re.sub("[\n,.;@#?!&$]+", " ", inp.lower()).split(" "))
    )


def searchres(req):
    query = req.POST["query"]
    query_encoding = model.encode(query)

    results = QuestionAnswer.objects.all()
    if req.POST["lecturer"] != "all":
        results = results.filter(recording__lecturer__id=req.POST["lecturer"])
    if req.POST["category"] != "all":
        results = results.filter(recording__category__id=req.POST["category"])
    if req.POST["date_from"] != "":
        results = results.filter(
            recording__date__gte=datetime.strptime(req.POST["date_from"], "%Y-%m-%d")
        )
    if req.POST["date_to"] != "":
        results = results.filter(
            recording__date__lte=datetime.strptime(req.POST["date_from"], "%Y-%m-%d")
        )
    similarities = [
        1 - distance.cosine(query_encoding, frombuffer(r.encoding, dtype=single))
        for r in results
    ]
    importances = [
        COEFFS[0] * heuristic(query, r.question)
        + COEFFS[1] * heuristic(query, r.preamble)
        + COEFFS[2] * heuristic(query, r.answer)
        for r in results
    ]
    scores = []
    for i in range(len(importances)):
        scores.append(similarities[i] + importances[i])

    ranks = argsort(scores)[-10:][::-1]
    sorted_results = [results[int(i)] for i in ranks]

    return render(
        req, "seapanapp/searchres.html", {"query": query, "results": sorted_results}
    )


def category_detail(req, category_id):
    c = get_object_or_404(Category, pk=category_id)
    ls = c.recordings.order_by("-date")
    return render(
        req,
        "seapanapp/l_list.html",
        {
            "ls": ls,
            "title": f"Lectures filed as: {c.name}",
            "bartitle": f"{c.name} - Category -",
        },
    )


def lecturer_detail(req, lecturer_id):
    lec = get_object_or_404(Lecturer, pk=lecturer_id)
    ls = lec.recordings.order_by("-date")
    return render(
        req,
        "seapanapp/l_list.html",
        {
            "ls": ls,
            "title": f"Lectures by: {lec.name}",
            "bartitle": f"{lec.name} - Lecturer -",
        },
    )

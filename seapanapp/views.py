from functools import cache
from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.template import loader
from sentence_transformers import SentenceTransformer
from scipy.spatial import distance
from numpy import argsort, frombuffer, single
from django.db.models import F

from .models import Category, Lecturer, QuestionAnswer, Recording


model = SentenceTransformer("distilbert-base-nli-mean-tokens")
# model = {}

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
    return render(req, "seapanapp/search.html")


def searchres(req):
    query = req.POST["query"]
    query_encoding = model.encode(query)

    results = QuestionAnswer.objects.all()
    similarities = [
        1 - distance.cosine(query_encoding, frombuffer(r.encoding, dtype=single))
        for r in results
    ]
    ranks = argsort(similarities)[-10:][::-1]
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
        {"ls": ls, "title": f"Lectures filed as: {c.name}"},
    )


def lecturer_detail(req, lecturer_id):
    lec = get_object_or_404(Lecturer, pk=lecturer_id)
    ls = lec.recordings.order_by("-date")
    return render(
        req,
        "seapanapp/l_list.html",
        {"ls": ls, "title": f"Lectures by: {lec.name}"},
    )

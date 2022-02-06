from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.template import loader
from django.db.models import F

from .models import QuestionAnswer, Recording

# Create your views here.


def index(req):
    latest_qs = QuestionAnswer.objects.all()
    context = {"latest_qs": latest_qs}

    return render(req, "seapanapp/index.html", context)


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
    qs = l.questions.all()
    return render(req, "seapanapp/l_detail.html", {"l": l, "qs": qs})


def search(req):
    return render(req, "seapanapp/search.html")


def searchres(req):
    query = req.POST["query"]
    # TODO: NLP stuff
    results = QuestionAnswer.objects.all()

    return render(req, "seapanapp/searchres.html", {"query": query, "results": results})

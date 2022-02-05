from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.template import loader

from .models import QuestionAnswer

# Create your views here.


def index(req):
    latest_qs = QuestionAnswer.objects.all()
    output = ", ".join((q.question for q in latest_qs))
    context = {"latest_qs": latest_qs}

    template = loader.get_template("seapanapp/index.html")

    return render(req, "seapanapp/index.html", context)


def q_details(req, question_id):
    q = get_object_or_404(QuestionAnswer, pk=question_id)
    return render(req, "seapanapp/q_detail.html", {"q": q})

    return HttpResponse(f"Details for question {question_id}")

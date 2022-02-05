from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("q/<int:question_id>/", views.q_details, name="detail"),
]

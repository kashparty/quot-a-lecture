from django.urls import path

from . import views

app_name = "seapanapp"
urlpatterns = [
    path("", views.index, name="q_list"),
    path("question/<int:question_id>/", views.q_details, name="q_detail"),
    path("lecture/<int:lecture_id>/", views.lecture_detail, name="lecture_detail"),
    path("search", views.search, name="search"),
    path("searchres", views.searchres, name="search_res"),
]

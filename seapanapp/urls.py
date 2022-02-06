from django.urls import path

from . import views

app_name = "seapanapp"
urlpatterns = [
    path("", views.index, name="search"),
    path("question/<int:question_id>/", views.q_details, name="q_detail"),
    path("question/<int:question_id>/upvote", views.q_upvote, name="q_upvote"),
    path("question/<int:question_id>/downvote", views.q_downvote, name="q_downvote"),
    path("lecture/<int:lecture_id>/", views.lecture_detail, name="lecture_detail"),
    path("lecturer/<int:lecturer_id>/", views.lecturer_detail, name="lecturer_detail"),
    path("category/<int:category_id>/", views.category_detail, name="category_detail"),
    path("lectures", views.lectures, name="l_list"),
    path("searchres", views.searchres, name="search_res"),
]

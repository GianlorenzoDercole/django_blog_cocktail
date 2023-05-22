from django.urls import path

from . import views

urlpatterns = [
    # home page
    path("", views.starting_page, name="starting-page"),
    # posts page
    path("posts", views.posts, name="posts-page"),
    # post page - slug is unique identifier
    path("posts/<slug:slug>", views.post_detail, name="post-detail-page")
    ]

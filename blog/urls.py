from django.urls import path
from .views import hello_view, about_view, PostNewsView, post_news_detail_view

urlpatterns = [
    path("hello/", hello_view, name="hello"),
    path("about/", about_view, name="about"),
    path("", PostNewsView.as_view(), name="news"),
    path("news/<int:id>/", post_news_detail_view, name="news_detail"),
]

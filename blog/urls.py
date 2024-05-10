from django.urls import path
from .views import hello_view, about_view, post_news_view, post_news_detail_view

urlpatterns = [
    path('hello/', hello_view, name='hello'),
    path('about/', about_view, name='about'),
    path('', post_news_view, name='news'),
    path('news/<int:id>/', post_news_detail_view, name='news_detail'),
]

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import PostNews


# Не полная информация
def post_news_view(request):
    if request.method == 'GET':
        posts = PostNews.objects.filter().order_by('-id')
        return render(request, template_name='post.html',
                      context={'posts': posts})




# Подробная информация при клике на кнопку подробнее
def post_news_detail_view(request, id):
    if request.method == 'GET':
        post_id = get_object_or_404(PostNews, id=id)
        return render(request, template_name='post_detail.html',
                      context={'post_id': post_id})


def hello_view(request):
    if request.method == 'GET':
        return HttpResponse('Ура это твой первый запрос на DJANGO-TEMPLATES')


def about_view(request):
    if request.method == 'GET':
        return HttpResponse('Меня зовут Радомир я Backend Developer')

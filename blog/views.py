from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import PostNews, VideoContent
from django.views import generic


class PostNewsView(generic.ListView):
    model = PostNews
    template_name = 'post.html'
    context_object_name = 'posts'
    ordering = ['-id']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['video_content'] = VideoContent.objects.order_by('-id')
        return context


# Не полная информация
# def post_news_view(request):
#     if request.method == "GET":
#         posts = PostNews.objects.filter().order_by("-id")
#         video_content = VideoContent.objects.filter().order_by("-id")
#         return render(request, template_name="post.html", context={
#             "posts": posts,
#             "video_content": video_content
#         })


# Подробная информация при клике на кнопку подробнее
def post_news_detail_view(request, id):
    if request.method == "GET":
        post_id = get_object_or_404(PostNews, id=id)
        return render(
            request, template_name="post_detail.html", context={"post_id": post_id}
        )


def hello_view(request):
    if request.method == "GET":
        return HttpResponse("Ура это твой первый запрос на DJANGO-TEMPLATES")


def about_view(request):
    if request.method == "GET":
        return HttpResponse("Меня зовут Радомир я Backend Developer")

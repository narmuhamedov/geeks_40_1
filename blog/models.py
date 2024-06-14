from django.db import models


class PostNews(models.Model):
    CATEGORY_NEWS = (
        ("Спорт", "Спорт"),
        ("Бизнес", "Бизнес"),
        ("Шоу бизнес", "Шоу бизнес"),
        ("Мир", "Мир"),
    )

    title = models.CharField(
        max_length=50, verbose_name="Напишите название новости", null=True
    )
    image = models.ImageField(
        upload_to="images/", verbose_name="Загрузите фото", blank=True
    )
    description = models.TextField(verbose_name="Напишите новость")
    music = models.FileField(
        upload_to="audio/", verbose_name="Загрузите песню", blank=True
    )
    video = models.URLField(verbose_name="Укажите видео ссылку")
    category_news = models.CharField(
        max_length=100, choices=CATEGORY_NEWS, verbose_name="Выберите категорию"
    )
    time_news = models.PositiveIntegerField(verbose_name="Укажите время новости")
    author = models.CharField(max_length=100, verbose_name="Укажите автора", null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.created_at}"

    class Meta:
        verbose_name = "новость"
        verbose_name_plural = "список новостей"


class VideoContent(models.Model):
    title = models.CharField(max_length=100)
    url_video = models.URLField()

    def __str__(self):
        return self.title

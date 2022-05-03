from django.db import models
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=30, verbose_name="Название")
    text = models.TextField(blank=True, verbose_name="Текст")
    img = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Картинка")
    time_create = models.DateField(auto_now_add=True, verbose_name="Время создания")
    time_update = models.DateField(auto_now=True, verbose_name="Время последнего обновления")
    author = models.CharField(max_length=100, verbose_name="Автор")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post", kwargs={"post_slug": self.slug})

    class Meta:
        verbose_name="Пост"
        verbose_name_plural="Посты"
    


from django.db import models
from django.contrib.auth.models import User


def user_directory_path(instance, filename):
    return "user_{0}/{1}".format(instance.user.id, filename)


class Articles(models.Model):
    title = models.CharField('Название', max_length=50)
    anons = models.CharField('Анонс', max_length=250)
    full_text = models.TextField('Статья')
    date = models.DateField('Дата публикации')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/news/{self.id}'

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


class MakePhotos(models.Model):
    user = models.ForeignKey(to=User, null=True, on_delete=models.SET_NULL)
    title = models.CharField('Название', max_length=50)
    full_text = models.TextField('Статья')
    date = models.DateField('Дата публикации')
    picture = models.ImageField(upload_to=user_directory_path)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Коллекция'
        verbose_name_plural = 'Коллекции'

    class Foo(models.Model):
        # Указывает на абсолютный путь
        audio = models.FilePathField(path='/home/user/')

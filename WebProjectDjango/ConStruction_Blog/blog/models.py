from django.db import models

# Create your models here.
'''
id
title
content
created_at
photo
'''


class Article(models.Model):

    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)      # атрибут blank - настравивает обязательность заполнения
    created_at = models.DateTimeField(auto_now_add=True)       # auto_now_add - единаждая дата сохранения
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')    # папка будет загружать картинки согласно году, мес, дню

    def __str__(self):
        return self.title


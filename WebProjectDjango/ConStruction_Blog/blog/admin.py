from django.contrib import admin
from .models import Article

# класс настраивает представление модели


class ArticleAdmin(admin.ModelAdmin):
    # отображение id и title в списке Действий в админ панели
    list_display = ('id', 'title', 'photo')
    # ссылки на статью по id и title
    list_display_links = ('id', 'title', 'photo')
    # поисковое поле по названию статьи и контенту
    search_fields = ('title', 'content')

# Register your models here.
admin.site.register(Article, ArticleAdmin)


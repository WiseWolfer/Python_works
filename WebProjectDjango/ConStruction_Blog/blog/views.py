from django.shortcuts import render
from django.http import HttpResponse
from .models import Article


def home(request):
    # order_by('-created_at') -  сортировка по убыванию
    # all() - просто получаем все данные из таблицы Article
    posts = Article.objects.order_by('-created_at')
    return render(request, 'blog/home.html', {'posts': posts})
    # res = '<h1>Список статей</h1>'
    # for post in posts:
    #     res += f'<div><h3>{post.title}</h3><div>{post.content}</div></div><hr>'
    # print(posts)
    # return HttpResponse(res)


def test(request):
    return HttpResponse('<h1>Test page!</h1>')

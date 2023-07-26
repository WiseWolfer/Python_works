# из локального каталога(приложения) импортируем файл views
from django.urls import path, include
from . import views

# отслеживаем сайты
urlpatterns = [
    # если пользователь на главной странцы, то обращаемся к методу индекс файла views
    # '' - главная страница (первое, куда мы попадаем)
    path('', views.index, name="home"),
    path('about', views.about, name="about"),
    path('contacts', views.contacts, name="contacts")
]
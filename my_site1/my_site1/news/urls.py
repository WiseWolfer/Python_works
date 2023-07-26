# из локального каталога(приложения) импортируем файл views
from django.urls import path
from . import views


# отслеживаем сайты
urlpatterns = [
    path('', views.news_home, name="news_home"),
    path('collection', views.collection_page, name="collection_page"),
    path('<int:pk>', views.NewDetailView.as_view(), name='news-detail'),
]

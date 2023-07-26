from django.shortcuts import render
from .models import Articles
from .models import MakePhotos
from django.views.generic import DetailView


def news_home(request):
    news = Articles.objects.order_by('-date')
    return render(request, 'news/news_home.html', {'news': news})


class NewDetailView(DetailView):
    model = Articles
    template_name = 'news/details_view.html'
    context_object_name = 'article'


def collection_page(request):
    collection = MakePhotos.objects.all()
    return render(request, 'news/news_pictures.html', {'collection': collection})


from django.urls import path
from .views import home, test

urlpatterns = [
    path('', home),
    path('test/', test),
]

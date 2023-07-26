from .import views
from django.urls import path, include

urlpatterns = [
    path('', views.index),
    path('transactions', views.transactions, name="res")
]

from django.urls import path
from .views import MainPage, ListPage

urlpatterns = [
  path('', MainPage, name="MainPage"),
  path('<str:list_name>/', ListPage, name="ListPage"),
]
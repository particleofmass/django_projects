from django.urls import path
from . import views

urlpatterns = [
    path('', views.mainpage, name='mainpage'),
    path('polls/', views.polls, name='polls'),
]

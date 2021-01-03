from django.contrib import admin
from django.urls import path
from . import views

app_name = 'app'
urlpatterns = [
    path('', views.index, name='index'),
    path('movies/', views.movies, name='movies'),
    path('movies/<int:id>/', views.movie, name='movie'),
    path('movie/edit/<int:id>/', views.edit, name='edit'),
    path('movie/new/', views.new, name='new')
]
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index_reviews'),
    path('int/<int:br>', views.broj, name='br_reviews'),
    path('int/', views.broj, name='br_reviews_def'),
    path('str/', views.rec, name='rec_reviews_def'),
    path('str/<str:word>', views.rec, name='rec_reviews'),
    path('params/', views.params, name='params_reviews'),
]
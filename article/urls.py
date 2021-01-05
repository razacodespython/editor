from django.contrib import admin
from django.urls import path
from article import views

urlpatterns = [
    path('', views.home, name = "home"),
    path('article/', views.article, name = "article"),
    path('articledownload/', views.articledownload, name = "articledownload"),
]
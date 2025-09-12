from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:name>", views.wiki, name="wiki"),
    path("newpage", views.newpage, name="newpage"),
    path("random/", views.randompage, name="randompage"),
    path("edit/<str:name>", views.edit, name="edit"),
    path("search/", views.search, name="search")
]

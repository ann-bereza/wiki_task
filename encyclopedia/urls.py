from django.urls import path

from encyclopedia import views

urlpatterns = [
    path("", views.index, name="index"),
    path("create", views.create_new_page, name="create"),
    path("search", views.search, name="search"),
    path("edit/<str:title>", views.edit_page, name="edit"),
    path("random", views.random_page, name="random"),
    path("wiki/<str:title>", views.open_entry, name="open"),

]

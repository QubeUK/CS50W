from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/create/", views.new_page, name="create"),
    path("wiki/random/", views.random, name="random"),
    path("display/", views.random, name="display")
]

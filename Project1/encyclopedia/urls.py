from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("/new_page", views.new_page, name="new_page"),
    path("/random", views.random, name="random")
    
]

from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.new_page, name="create"),
    path("random/", views.random, name="random")
    
]

from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("", views.new_page, name="new_page")
    
]

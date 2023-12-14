from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/create/", views.new_page, name="create"),
    path("wiki/rand/", views.rand, name="rand"),
    path("wiki/display/", views.display, name="display"),
    #path("<str:entry>/", views.rand, name="entry")

]

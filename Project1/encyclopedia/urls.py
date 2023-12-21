from django.urls import path

from . import views

app_name = "wiki"
urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/create/", views.new_page, name="create"),
    path("wiki/rand/", views.rand, name="rand"),
    path("wiki/<str:article>/", views.display, name="display"),
    path("query", views.search, name ="search"),
    path("wiki/edit", views.edit, name ="edit"),
]

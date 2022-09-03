from django.urls import path
from . import views

app_name = "article"

urlpatterns = [
    path("article/<int:id>", views.article, name="article"),
    path("", views.about, name="home"),
]
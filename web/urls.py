from django.urls import path
from . import views

urlpatterns = [
    path("", view=views.index),
    path("lyrics/<slug:slug>", view=views.song_lyrics),
    path("singers", view=views.all_singers),
    path("writers", view=views.all_writers),
    path("search", view=views.search),
]
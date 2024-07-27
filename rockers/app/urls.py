from django.urls import path
from . import views

urlpatterns = [
    path("", view=views.index),
    path("lyrics/<slug:slug>", view=views.song_lyrics),
    path("artists", view=views.all_artists),
    path("search", view=views.search),
]
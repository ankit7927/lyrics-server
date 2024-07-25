from django.urls import path, include
from . import views

song_urlpatterns = [
    path("create", view=views.create_song),
    path("<int:id>/get", view=views.song_by_id),
]

urlpatterns = [
    path("song/", include(song_urlpatterns)),
    path("home-feed", view=views.home_feed), 
]


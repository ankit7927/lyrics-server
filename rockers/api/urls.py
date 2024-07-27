from django.urls import path, include
from . import views

song_urlpatterns = [
    path("create", view=views.create_song),
    path("<int:id>/get", view=views.song_by_id),
]

collection_urlpatterns = [
    path("", view=views.all_collections),
    path("<int:id>", view=views.collection_by_id)
]

urlpatterns = [
    path("song/", include(song_urlpatterns)),
    path("coll/", include(collection_urlpatterns)),
    path("home-feed", view=views.home_feed),
    path("search", view=views.search_song),
]


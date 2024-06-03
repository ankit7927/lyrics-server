from django.urls import path, include
from .views import song, album, singer, writer, common

album_urlpatterns = [
    path("all", view=album.get_all_album),
    path("<int:id>/get", view=album.get_album),
    path("<int:id>/songs", view=song.get_album_song),
    path("create", view=album.create_album),
    path("search", view=album.search_album),
]

singer_urlpatterns = [
    path("all", view=singer.get_all_singer),
    path("<int:id>/get", view=singer.get_singer),
    path("<int:id>/songs", view=song.get_singer_song),
    path("create", view=singer.create_singer),
    path("search", view=singer.search_singer),
]

writer_urlpatterns = [
    path("all", view=writer.get_all_writer),
    path("<int:id>/get", view=writer.get_writer),
    path("<int:id>/songs", view=song.get_writer_song),
    path("create", view=writer.create_writer),
    path("search", view=writer.search_writer),
]

song_urlpatterns = [
    path("all", view=song.get_all_songs),
    path("create", view=song.create_song),
    path("<int:id>/get", view=song.get_song_id),
    path("<int:id>/delete", view=song.delete_song),
    path("search", view=song.search_song),
]

common_urlpatterns = [
    path("home-feed", view=common.get_home_content),
]

urlpatterns = [
    path("song/", include(song_urlpatterns)),
    path("album/", include(album_urlpatterns)),
    path("singer/", include(singer_urlpatterns)),
    path("writer/", include(writer_urlpatterns)),
    path("common/", include(common_urlpatterns)),
]


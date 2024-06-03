from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from services import song_service as songs
from services import singer_service as singers
from services import writer_service as writers

def index(request, singer=None, album=None):
    singer=request.GET.get("singer", None)
    album=request.GET.get("album", None)
    writer=request.GET.get("writer", None)

    songs_data = None

    if singer:
        songs_data = songs.get_singer_song(singer_name=singer).order_by("created")
    if album:
        songs_data = songs.get_album_song(album_name=album).order_by("created")
    if writer:
        songs_data = songs.get_writer_song(writer_name=writer).order_by("created")
    if songs_data is None: 
        songs_data = songs.get_all_songs().values("name", "thumbnail", "slug").order_by("created")

    paginator = Paginator(object_list=songs_data, per_page=25)
    page_songs_data = paginator.get_page(1 if request.GET.get("page") is None else request.GET.get("page"))

    return render(request=request, template_name="index.html", context={"songs":page_songs_data})


def song_lyrics(request, slug):
    try:
        song_data = songs.get_song_by_slug(slug=slug)

        album_songs = songs.get_album_song(album_id=song_data.album.id).exclude(id=song_data.id)[:5]
        singers_songs = songs.get_singers_song(song_data.singer.all()).exclude(id=song_data.id)[:5]
        writers_songs = songs.get_writers_song(song_data.writer.all()).exclude(id=song_data.id)[:5]

        return render(request=request, template_name="lyrics.html", context={"lyrics":song_data, "singer_songs":singers_songs, "album_songs":album_songs, "writer_songs":writers_songs})
    except Exception as e:
        print(e)
        return render(request=request, template_name="notfound.html")
    
def all_singers(request):
    singers_data = singers.get_all_singer()
    paginator = Paginator(object_list=singers_data, per_page=25)
    page_singers = paginator.get_page(1 if request.GET.get("page") is None else request.GET.get("page"))

    return render(request=request, template_name="singers.html", context={"singers":page_singers})


def all_writers(request):
    writers_data = writers.get_all_writer()
    paginator = Paginator(object_list=writers_data, per_page=25)
    page_writers = paginator.get_page(1 if request.GET.get("page") is None else request.GET.get("page"))

    return render(request=request, template_name="writers.html", context={"writers":page_writers})

def search(request):
    query=request.GET.get("query", None)

    try:
        if query != "":
            response = songs.search_song(query=query)
            return render(request=request, template_name="index.html", context={"songs":response})
        else: return redirect(to="/")
    except Exception as e:
        return redirect(to="/")
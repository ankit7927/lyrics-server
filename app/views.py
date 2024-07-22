from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.db.models import Q
from .models import SongModel, SingerModel, WriterModel

def index(request, singer=None, album=None):
    singer=request.GET.get("singer", None)
    album=request.GET.get("album", None)
    writer=request.GET.get("writer", None)

    songs_data = None

    if singer:
        songs_data = SongModel.objects.filter(singer__name=singer)
    if album:
        songs_data = SongModel.objects.filter(album__name=album)
    if writer:
        songs_data = SongModel.objects.filter(writer__name=writer)
    if songs_data is None: 
        songs_data = SongModel.objects.all().values("name", "thumbnail", "slug").order_by("created")

    paginator = Paginator(object_list=songs_data, per_page=25)
    page_songs_data = paginator.get_page(1 if request.GET.get("page") is None else request.GET.get("page"))

    return render(request=request, template_name="index.html", context={"songs":page_songs_data})


def song_lyrics(request, slug):
    try:
        song_data = SongModel.objects.get(slug=slug)

        album_songs = SongModel.objects.filter(album__id=song_data.album.id).exclude(id=song_data.id)[:5]
        singers_songs = SongModel.objects.filter(singer__in=song_data.singer.all()).distinct().exclude(id=song_data.id)[:5]
        writers_songs = SongModel.objects.filter(writer__in=song_data.writer.all()).exclude(id=song_data.id)[:5]

        return render(request=request, template_name="lyrics.html", context={"lyrics":song_data, "singer_songs":singers_songs, "album_songs":album_songs, "writer_songs":writers_songs})
    except Exception as e:
        print(e)
        return render(request=request, template_name="notfound.html")
    
def all_singers(request):
    singers_data = SingerModel.objects.all()
    paginator = Paginator(object_list=singers_data, per_page=25)
    page_singers = paginator.get_page(1 if request.GET.get("page") is None else request.GET.get("page"))

    return render(request=request, template_name="singers.html", context={"singers":page_singers})


def all_writers(request):
    writers_data = WriterModel.objects.all()
    paginator = Paginator(object_list=writers_data, per_page=25)
    page_writers = paginator.get_page(1 if request.GET.get("page") is None else request.GET.get("page"))

    return render(request=request, template_name="writers.html", context={"writers":page_writers})

def search(request):
    query=request.GET.get("query", None)

    try:
        if query != "":
            response = SongModel.objects.filter(
                Q(name__icontains=query) |
                Q(music__icontains=query) |
                Q(lyrics__icontains=query))
            
            return render(request=request, template_name="index.html", context={"songs":response})
        else: return redirect(to="/")
    except Exception as e:
        return redirect(to="/")
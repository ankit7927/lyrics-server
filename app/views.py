from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.db.models import Q
from .models import SongModel, ArtistModel

def index(request, artist=None, album=None):
    artist=request.GET.get("artist", None)
    album=request.GET.get("album", None)

    songs_data = None

    if artist:
        songs_data = SongModel.objects.filter(artist__name=artist).order_by("created")
    if album:
        songs_data = SongModel.objects.filter(album__name=album).order_by("created")

    if songs_data is None: 
        songs_data = SongModel.objects.all().values("name", "thumbnail", "slug").order_by("created")

    paginator = Paginator(object_list=songs_data, per_page=25)
    page_songs_data = paginator.get_page(1 if request.GET.get("page") is None else request.GET.get("page"))

    return render(request=request, template_name="index.html", context={"songs":page_songs_data})


def song_lyrics(request, slug):
    try:
        song_data = SongModel.objects.get(slug=slug)

        album_songs = SongModel.objects.filter(album__id=song_data.album.id).exclude(id=song_data.id)[:5]
        artists_songs = SongModel.objects.filter(artist__in=song_data.artist.all()).distinct().exclude(id=song_data.id)[:5]

        return render(request=request, template_name="lyrics.html", context={"lyrics":song_data, "artist_songs":artists_songs, "album_songs":album_songs})
    except Exception as e:
        print(e)
        return render(request=request, template_name="notfound.html")
    
def all_artists(request):
    artist_data = ArtistModel.objects.all().order_by("name")
    paginator = Paginator(object_list=artist_data, per_page=25)
    page_artists = paginator.get_page(1 if request.GET.get("page") is None else request.GET.get("page"))

    return render(request=request, template_name="artists.html", context={"artists":page_artists})

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
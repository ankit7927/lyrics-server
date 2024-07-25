from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from app.models import SongModel, AlbumModel, ArtistModel
from .serializers import SongBasicSerializer, SongSerializer, ArtistBasicSerializer
import datetime

@api_view(http_method_names=["GET"])
def home_feed(request):
    top_songs = SongModel.objects.all()[:7]
    latest_song = SongModel.objects.all()[7:21]
    artists = SongModel.objects.all()[:9]

    response = {
        "popular": SongBasicSerializer(instance=top_songs, many=True).data,
        "latest": SongBasicSerializer(instance=latest_song, many=True).data,
        "artist": ArtistBasicSerializer(instance=artists, many=True).data
    }

    return Response(data=response)

@api_view(http_method_names=["GET"])
def song_by_id(request, id):
    if id == "" : return Response(data={"error":"id is not provided"}, status=status.HTTP_400_BAD_REQUEST)
    try:
        song = SongModel.objects.get(id=id)
        song_ser = SongSerializer(instance=song)
        return Response(data=song_ser.data)
    except Exception as e:
        print(e)
        return Response(data={"error":"something wrong"}, status=status.HTTP_503_SERVICE_UNAVAILABLE)
    
@api_view(http_method_names=["POST"])
def create_song(request):
    song_data = request.data

    if song_data["album"]:
        alb, _ = AlbumModel.objects.get_or_create(name=song_data["album"])

    if song_data["artist"]:
        artists = []
        for artist in song_data["artist"]:
            artists.append(ArtistModel.objects.get_or_create(name=artist)[0])

    new_song = SongModel.objects.create(
        name = song_data["name"],
        music = song_data["music"],
        lyrics = song_data["lyrics"],
        ytvid = song_data["ytvid"],
        slug = song_data["slug"], 
        created = datetime.datetime.fromisoformat(song_data["publish"]),
        album = alb)

    if song_data["thumbnail"] == "":
        new_song.thumbnail = request.build_absolute_uri("/static/song-thumbnail-notfound.png")
    else:
        new_song.thumbnail = song_data["thumbnail"]

    new_song.artist.set(artists)
    new_song.save()
        
    return Response(data={"message":"song created"})


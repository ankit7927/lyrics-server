from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from app.models import SongModel, SingerModel
from .serializer.song import SongBasicSerializer, SongSerializer
from .serializer.singer import SingerBasicSerializer

@api_view(http_method_names=["GET"])
def home_feed(request):
    top_songs = SongModel.objects.all()[:5]
    latest_song = SongModel.objects.all()[6:14]
    singers = SongModel.objects.all()[:6]

    response = {
        "top": SongBasicSerializer(instance=top_songs, many=True).data,
        "latest": SongBasicSerializer(instance=latest_song, many=True).data,
        "singers": SingerBasicSerializer(instance=singers, many=True).data
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
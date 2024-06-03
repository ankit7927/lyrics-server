from rest_framework.decorators import api_view
from rest_framework.response import Response
from services import song_service as songs
from services import singer_service as singers
from serializer.song import SongSerializer, SongBasicSerializer
from serializer.singer import SingerSerializer, SingerBasicSerializer


# top searched
# latest, populor singers

@api_view(["GET"])
def get_home_content(request):
    latest = songs.get_all_songs()
    singer = singers.get_all_singer()
    popular = songs.get_latest_songs()

    response = {
        "latestSongs" : SongBasicSerializer(instance=latest, many=True).data,
        "topSingers" : SingerBasicSerializer(instance=singer, many=True).data,
        "popularSongs" : SongBasicSerializer(instance=popular, many=True).data,
    }

    return Response(data=response)


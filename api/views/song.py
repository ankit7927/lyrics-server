from rest_framework.decorators import api_view
from rest_framework.response import Response
from services import song_service as songs
from serializer.song import SongSerializer, SongBasicSerializer

@api_view(["GET"])
def get_all_songs(request):
    songs_data = songs.get_all_songs()
    serialized = SongSerializer(instance=songs_data, many=True)
    return Response(data=serialized.data)


@api_view(["GET"])
def get_song_slug(request, slug):
    try:
        song_data = songs.get_song_by_slug(slug=slug)
        serialized = SongSerializer(instance=song_data)
        return Response(data=serialized.data)
    except:
        return Response(data={"message":"song not found"}, status=404)
    
@api_view(["GET"])
def get_song_id(request, id):
    try:
        song_data = songs.get_song_by_id(id=id)
        singers_songs = songs.get_singers_song(song_data.singer.all()).exclude(id=id)
        writers_songs = songs.get_writers_song(song_data.writer.all()).exclude(id=id)

        resp = {
            "song_data": SongSerializer(instance=song_data).data,
            "singers_songs": SongBasicSerializer(instance=singers_songs, many=True).data,
            "writers_songs": SongBasicSerializer(instance=writers_songs, many=True).data,
        }

        return Response(data=resp)
    except Exception as e:
        return Response(data={"message":"song not found"}, status=404)
    
@api_view(["GET"])
def get_album_song(request, id):
    try:
        song_data = songs.get_album_song(album_id=id)
        serialized = SongBasicSerializer(instance=song_data, many=True)
        return Response(data=serialized.data)
    except Exception as e:
        return Response(data={"message":"song not found"}, status=404)
    
@api_view(["GET"])
def get_singer_song(request, id):
    try:
        song_data = songs.get_singer_song(singer_id=id)
        serialized = SongBasicSerializer(instance=song_data, many=True)
        return Response(data=serialized.data)
    except Exception as e:
        return Response(data={"message":"song not found"}, status=404)

@api_view(["GET"])
def get_writer_song(request, id):
    try:
        song_data = songs.get_writer_song(writer_id=id)
        serialized = SongBasicSerializer(instance=song_data, many=True)
        return Response(data=serialized.data)
    except Exception as e:
        return Response(data={"message":"song not found"}, status=404)

@api_view(["POST"])
def create_song(request):
    try:
        response = songs.create_song(song_data=request.data)
        return Response(data=response)
    except Exception as e:
        return Response(data={"message":"failed to create song"}, status=404)
    
@api_view(["DELETE"])
def delete_song(request, id):
    try:
        response = songs.delete_song(id=id)
        return Response(data=response)
    except Exception as e:
        return Response(data={"message":"failed to delete song"}, status=404)
    
@api_view(["GET"])
def search_song(request):
    query=request.GET.get("query", None)

    try:
        if query != "":
            response = songs.search_song(query=query)
            serialized = SongBasicSerializer(instance=response, many=True)
            return Response(data=serialized.data)
        else: return Response(data={"message":"empty query not allowd"}, status=404)
    except Exception as e:
        return Response(data={"message":"something went wrong"}, status=500)



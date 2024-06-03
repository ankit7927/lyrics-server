from rest_framework.decorators import api_view
from rest_framework.response import Response
from services import album_service as albums
from serializer.album import AlbumBasicSerializer, AlbumSerializer


@api_view(["GET"])
def get_all_album(request):
    album_data = albums.get_all_album()
    serialized = AlbumBasicSerializer(instance=album_data, many=True)
    return Response(data=serialized.data)


@api_view(["GET"])
def get_album(request, id):
    try:
        album_data = albums.get_album(id=id)
        serialized = AlbumSerializer(instance=album_data)
        return Response(data=serialized.data)
    except:
        return Response(data={"message":"album not found"}, status=404)
    

@api_view(["DELETE"])
def delete_album(request, id):
    try:
        response = albums.delete_album(id=id)
        return Response(data=response)
    except:
        return Response(data={"message":"failed to delete album"}, status=404)


@api_view(["POST"])
def create_album(request):
    try:
        response = albums.create_album(album_data=request.data)
        serialized = AlbumSerializer(instance=response)
        return Response(data=serialized.data)
    except Exception as e:
        return Response(data={"message":"failed to create album"}, status=404)
    

@api_view(["GET"])
def search_album(request):
    query=request.GET.get("query", None)

    try:
        if query != "":
            response = albums.search_album(query=query)
            serialized = AlbumBasicSerializer(instance=response, many=True)
            return Response(data=serialized.data)
        else: return Response(data={"message":"empty query not allowd"}, status=404)
    except Exception as e:
        return Response(data={"message":"something went wrong"}, status=500)

    
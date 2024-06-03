from rest_framework.decorators import api_view
from rest_framework.response import Response
from services import singer_service as singer
from serializer.singer import SingerBasicSerializer, SingerSerializer


@api_view(["GET"])
def get_all_singer(request):
    singer_data = singer.get_all_singer()
    serialized = SingerBasicSerializer(instance=singer_data, many=True)
    return Response(data=serialized.data)


@api_view(["GET"])
def get_singer(request, id):
    try:
        singer_data = singer.get_singer(id=id)
        serialized = SingerSerializer(instance=singer_data)
        return Response(data=serialized.data)
    except:
        return Response(data={"message":"singer not found"}, status=404)
    

@api_view(["DELETE"])
def delete_singer(request, id):
    try:
        response = singer.delete_singer(id=id)
        return Response(data=response)
    except:
        return Response(data={"message":"failed to delete singer"}, status=404)


@api_view(["POST"])
def create_singer(request):
    try:
        response = singer.create_singer(singer_data=request.data)
        serialized = SingerSerializer(instance=response)
        return Response(data=serialized.data)
    except Exception as e:
        return Response(data={"message":"failed to create singer"}, status=404)


@api_view(["GET"])
def search_singer(request):
    query=request.GET.get("query", None)

    try:
        if query != "":
            response = singer.search_singer(query=query)
            serialized = SingerBasicSerializer(instance=response, many=True)
            return Response(data=serialized.data)
        else: return Response(data={"message":"empty query not allowd"}, status=404)
    except Exception as e:
        return Response(data={"message":"something went wrong"}, status=500)

    
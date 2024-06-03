from rest_framework.decorators import api_view
from rest_framework.response import Response
from services import writer_service as writer
from serializer.writer import WriterBasicSerializer, WriterSerializer


@api_view(["GET"])
def get_all_writer(request):
    writer_data = writer.get_all_writer()
    serialized = WriterBasicSerializer(instance=writer_data, many=True)
    return Response(data=serialized.data)


@api_view(["GET"])
def get_writer(request, id):
    try:
        writer_data = writer.get_writer(id=id)
        serialized = WriterSerializer(instance=writer_data)
        return Response(data=serialized.data)
    except:
        return Response(data={"message":"writer not found"}, status=404)
    

@api_view(["DELETE"])
def delete_writer(request, id):
    try:
        response = writer.delete_writer(id=id)
        return Response(data=response)
    except:
        return Response(data={"message":"failed to delete writer"}, status=404)


@api_view(["POST"])
def create_writer(request):
    try:
        response = writer.create_writer(writer_data=request.data)
        serialized = WriterSerializer(instance=response)
        return Response(data=serialized.data)
    except Exception as e:
        return Response(data={"message":"failed to create writer"}, status=404)
    

@api_view(["GET"])
def search_writer(request):
    query=request.GET.get("query", None)

    try:
        if query != "":
            response = writer.search_writer(query=query)
            serialized = WriterBasicSerializer(instance=response, many=True)
            return Response(data=serialized.data)
        else: return Response(data={"message":"empty query not allowd"}, status=404)
    except Exception as e:
        return Response(data={"message":"something went wrong"}, status=500)

    
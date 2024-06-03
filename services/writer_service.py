from core.models import WriterModel
from django.db.models import Q


def get_all_writer()-> list[WriterModel]:
    return WriterModel.objects.all()

def get_writer(id:int)-> WriterModel:
    return WriterModel.objects.get(id=id)

def create_writer(writer_data)-> WriterModel:
    return WriterModel.objects.create(name=writer_data["name"], description=writer_data["description"], image=writer_data["image"])

def delete_writer(id:int):
    writer = WriterModel.objects.get(id=id)
    writer.delete()
    return {"message":"writer deleted"}

def search_writer(query:str):
    response = WriterModel.objects.filter(
        Q(name__icontains=query) |
        Q(description__icontains=query))
    return response
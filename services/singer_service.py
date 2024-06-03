from core.models import SingerModel
from django.db.models import Q
def get_all_singer()-> list[SingerModel]:
    return SingerModel.objects.all()

def get_singer(id:int)-> SingerModel:
    return SingerModel.objects.get(id=id)

def create_singer(singer_data)-> SingerModel:
    return SingerModel.objects.create(name=singer_data["name"], description=singer_data["description"], image=singer_data["image"])

def delete_singer(id:int):
    singer = SingerModel.objects.get(id=id)
    singer.delete()
    return {"message":"singer deleted"}

def search_singer(query:str):
    response = SingerModel.objects.filter(
        Q(name__icontains=query) |
        Q(description__icontains=query))
    return response
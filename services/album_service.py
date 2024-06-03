from core.models import AlbumModel
from django.db.models import Q


def get_all_album()-> list[AlbumModel]:
    return AlbumModel.objects.all()

def get_album(id:int)-> AlbumModel:
    return AlbumModel.objects.get(id=id)

def create_album(album_data)-> AlbumModel:
    return AlbumModel.objects.create(name=album_data["name"], description=album_data["description"], image=album_data["image"])

def delete_album(id:int):
    album = AlbumModel.objects.get(id=id)
    album.delete()
    return {"message":"album deleted"}

def search_album(query:str):
    response = AlbumModel.objects.filter(
        Q(name__icontains=query) |
        Q(description__icontains=query))
    return response
from django.contrib import admin
from .models import SongModel, ArtistModel, AlbumModel, CollectionModel
# Register your models here.

admin.site.register((SongModel, ArtistModel, AlbumModel, CollectionModel))

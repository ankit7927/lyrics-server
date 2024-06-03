from django.contrib import admin
from .models import SingerModel, SongModel, WriterModel, AlbumModel

admin.site.register((SingerModel, SongModel, WriterModel, AlbumModel))

from django.contrib import admin
from .models import SingerModel, SongModel, WriterModel, AlbumModel
# Register your models here.

admin.site.register((SingerModel, SongModel, WriterModel, AlbumModel))

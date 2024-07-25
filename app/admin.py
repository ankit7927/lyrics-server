from django.contrib import admin
from .models import SongModel, ArtistModel, AlbumModel
# Register your models here.

admin.site.register((SongModel, ArtistModel, AlbumModel))

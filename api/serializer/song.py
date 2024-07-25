from rest_framework import serializers
from .artist import ArtistBasicSerializer
from .album import AlbumBasicSerializer
from .artist import ArtistBasicSerializer
from app.models import SongModel

class SongSerializer(serializers.ModelSerializer):
    singer = ArtistBasicSerializer(read_only=True, many=True)
    album = AlbumBasicSerializer(read_only=True)
    artist = ArtistBasicSerializer(read_only=True, many=True)

    class Meta:
        model = SongModel
        fields = "__all__"


class SongBasicSerializer(serializers.ModelSerializer):
    album = AlbumBasicSerializer(read_only=True)
    class Meta:
        model = SongModel
        fields = ["id", "name", "album", "thumbnail"]
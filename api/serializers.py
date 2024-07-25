from rest_framework import serializers
from app.models import AlbumModel, ArtistModel, SongModel

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlbumModel
        fields = "__all__"

class AlbumBasicSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlbumModel
        fields = ["id", "name", "image"]

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArtistModel
        fields = "__all__"

class ArtistBasicSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArtistModel
        fields = ["id", "name", "image"]

class SongSerializer(serializers.ModelSerializer):
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

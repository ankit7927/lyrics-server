from rest_framework import serializers
from app.models import AlbumModel, ArtistModel, SongModel, CollectionModel

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
        fields = ["id", "name"]

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

class CollectionSerializer(serializers.ModelSerializer):
    songs = SongBasicSerializer(read_only=True, many=True)
    class Meta:
        model = CollectionModel
        fields = "__all__"

class CollectionBasicSerializer(serializers.ModelSerializer):
    class Meta:
        model = CollectionModel
        fields = ["id", "name", "thumbnail"]
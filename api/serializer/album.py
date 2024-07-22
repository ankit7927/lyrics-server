from rest_framework import serializers
from app.models import AlbumModel

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlbumModel
        fields = "__all__"

class AlbumBasicSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlbumModel
        fields = ["id", "name", "image"]
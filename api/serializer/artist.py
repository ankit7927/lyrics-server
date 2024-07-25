from rest_framework import serializers
from app.models import ArtistModel

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArtistModel
        fields = "__all__"

class ArtistBasicSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArtistModel
        fields = ["id", "name", "image"]
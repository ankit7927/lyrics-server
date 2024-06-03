from rest_framework import serializers
from core.models import SingerModel

class SingerSerializer(serializers.ModelSerializer):
    class Meta:
        model = SingerModel
        fields = "__all__"

class SingerBasicSerializer(serializers.ModelSerializer):
    class Meta:
        model = SingerModel
        fields = ["id", "name", "image"]
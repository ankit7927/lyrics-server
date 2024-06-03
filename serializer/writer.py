from rest_framework import serializers
from core.models import WriterModel

class WriterSerializer(serializers.ModelSerializer):
    class Meta:
        model = WriterModel
        fields = "__all__"

class WriterBasicSerializer(serializers.ModelSerializer):
    class Meta:
        model = WriterModel
        fields = ["id", "name", "image"]
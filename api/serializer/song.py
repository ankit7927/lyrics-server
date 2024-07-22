from rest_framework import serializers
from .singer import SingerBasicSerializer
from .writer import WriterBasicSerializer
from .album import AlbumBasicSerializer
from app.models import SongModel

class SongSerializer(serializers.ModelSerializer):
    singer = SingerBasicSerializer(read_only=True, many=True)
    album = AlbumBasicSerializer(read_only=True)
    writer = WriterBasicSerializer(read_only=True, many=True)

    class Meta:
        model = SongModel
        fields = "__all__"


class SongBasicSerializer(serializers.ModelSerializer):
    class Meta:
        model = SongModel
        fields = ["id", "name", "album", "thumbnail"]
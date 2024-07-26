from django.db import models

class ArtistModel(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return self.name
    

class AlbumModel(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(null=True, blank=True)
    image = models.CharField(max_length=256, null=True, blank=True)

    def __str__(self) -> str:
        return self.name

class SongModel(models.Model):
    name = models.CharField(max_length=40)
    album = models.ForeignKey(AlbumModel, null=True, blank=True, on_delete=models.DO_NOTHING)
    artist = models.ManyToManyField(ArtistModel, blank=True)
    music = models.CharField(max_length=80, null=True, blank=True)
    thumbnail = models.CharField(max_length=256, default="/static/song-thumbnail-notfound.png")
    lyrics = models.TextField()
    ytvid = models.CharField(max_length=20, null=True, blank=True)
    slug = models.SlugField(max_length=80, null=True, unique=True)
    created = models.DateTimeField(null=True, blank=True)

    def __str__(self) -> str:
        return self.name

class CollectionModel(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField(null=True, blank=True)
    thumbnail = models.CharField(max_length=256)
    songs = models.ManyToManyField(to=SongModel)

    def __str__(self) -> str:
        return self.name
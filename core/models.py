from django.db import models

class AlbumModel(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(null=True, blank=True)
    image = models.CharField(max_length=256, null=True, blank=True)

    def __str__(self) -> str:
        return self.name

class SingerModel(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(null=True, blank=True)
    image = models.CharField(max_length=256, null=True, blank=True)

    def __str__(self) -> str:
        return self.name

class WriterModel(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(null=True, blank=True)
    image = models.CharField(max_length=256, null=True, blank=True)

    def __str__(self) -> str:
        return self.name

class SongModel(models.Model):
    name = models.CharField(max_length=40)
    album = models.ForeignKey(AlbumModel, null=True, blank=True, on_delete=models.DO_NOTHING)
    singer = models.ManyToManyField(SingerModel, blank=True)
    writer = models.ManyToManyField(WriterModel, blank=True)
    music = models.CharField(max_length=80, null=True, blank=True)
    thumbnail = models.CharField(max_length=256, null=True, blank=True, default="https://www.churchmotiongraphics.com/wp-content/uploads/2018/01/WorshipBackground.jpg")
    lyrics = models.TextField()
    ytvid = models.CharField(max_length=20, null=True, blank=True)
    slug = models.SlugField(max_length=80, null=True, unique=True)
    created = models.DateTimeField(null=True, blank=True)

    def __str__(self) -> str:
        return self.name

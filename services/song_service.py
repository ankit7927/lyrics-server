from core.models import SongModel, AlbumModel, SingerModel, WriterModel
from django.db.models import Q
import datetime


def get_all_songs():
    return SongModel.objects.all()

def get_song_by_slug(slug:str) -> SongModel:
    return SongModel.objects.get(slug=slug)

def get_song_by_id(id:int) -> SongModel:
    return SongModel.objects.get(id=id)

def get_album_song(album_id=None, album_name=None):
    if album_id:
        return SongModel.objects.filter(album__id=album_id)
    elif album_name:
        return SongModel.objects.filter(album__name=album_name)
    else: raise Exception("albums id or name is required")

def get_singer_song(singer_id=None, singer_name=None):
    if singer_id:
        return SongModel.objects.filter(singer__id=singer_id)
    elif singer_name:
        return SongModel.objects.filter(singer__name=singer_name)
    else: raise Exception("singers id or name is required")

def get_singers_song(singer_ids):
    return SongModel.objects.filter(singer__in=singer_ids).distinct()

def get_writer_song(writer_id=None, writer_name=None):
    if writer_id:
        return SongModel.objects.filter(writer__id=writer_id)
    elif writer_name:
        return SongModel.objects.filter(writer__name=writer_name)
    else: raise Exception("writers id or name is required")

def get_writers_song(writer_ids):
    return SongModel.objects.filter(writer__in=writer_ids)

def create_song(song_data):
    if song_data["album"]:
        alb, _ = AlbumModel.objects.get_or_create(name=song_data["album"])

    if song_data["singer"]:
        singers = []
        for singer in song_data["singer"]:
            singers.append(SingerModel.objects.get_or_create(name=singer)[0])

    if song_data["writer"]:
        writers = []
        for writer in song_data["writer"]:
            writers.append(WriterModel.objects.get_or_create(name=writer)[0])

    new_song = SongModel.objects.create(
        name = song_data["name"],
        music = song_data["music"],
        thumbnail = song_data["thumbnail"],
        lyrics = song_data["lyrics"],
        ytvid = song_data["ytvid"],
        slug = song_data["slug"], 
        created = datetime.datetime.fromisoformat(song_data["publish"]),
        album = alb)

    new_song.singer.set(singers)
    new_song.writer.set(writers)
        
    return {"message":"song created"}

def delete_song(id:int):
    test = SongModel.objects.get(id=id)
    test.delete()
    return {"message":"song seleted"}


def get_latest_songs():
    songs = SongModel.objects.order_by("created")


def search_song(query:str):
    response = SongModel.objects.filter(
        Q(name__icontains=query) |
        Q(music__icontains=query) |
        Q(lyrics__icontains=query))
    return response



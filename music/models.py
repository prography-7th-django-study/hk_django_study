from django.db import models
from datetime import datetime
from genre.models import Genre
from artist.models import Artist

def get_album_image_path(self, filename):
    ext = filename.split('.')[-1]
    filename = self.name + "." + ext
    return '/'.join(['album', filename]) 
        # through필드를 사용했기 때문에 self.artists.stage_name으로 가져오면 생성이 되기전에 가져오기때문에 에러남


class Album(models.Model):
    name = models.CharField(max_length=150)
    artists = models.ManyToManyField(Artist, through='ArtistAlbum', related_name='albums', blank=True)
    image = models.ImageField(upload_to=get_album_image_path)
    description = models.TextField()
    release_at = models.DateTimeField(default=datetime.now)
    ALBUM_TYPE = (
        ('AL', 'Album'),
        ('SG', 'Single'),
        ('DS', 'DigitalSingle'),
        ('MN', 'Mini'),
        ('RP', 'Repackage'),
        ('SA', 'SpecialAddition'),
        ('BL', 'Bootleg'),
        ('CO', 'Compilation'),
    )
    type = models.CharField(max_length=2, choices=ALBUM_TYPE)
    
    def __str__(self):
        return self.name

class ArtistAlbum(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.PROTECT)
    album = models.ForeignKey(Album, on_delete=models.PROTECT)
    
    def __str__(self):
        return "artist" + str(self.artist_id) + "'s album" + str(self.album_id)
  
class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, null=True, related_name='songs')
    featuring = models.CharField(max_length=150, blank=True, null=True)
    title = models.CharField(max_length=300)
    is_title = models.BooleanField(default=False) # song에서는 의미있는 정보가 아니므로 through사용~, 의미가 있다면 둬도 괜찮음
    lyrics = models.TextField()
    description = models.TextField()
    genre = models.ManyToManyField(Genre)
    duration = models.TimeField()
    released_date = models.DateField()

    def __str__(self):
        if self.is_title:
            return self.title + " [title]"
        return self.title
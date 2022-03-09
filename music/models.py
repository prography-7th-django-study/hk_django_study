from django.db import models
from datetime import datetime
from genre.models import Genre
from artist.models import Artist

def get_album_image_path(self, filename):
  ext = filename.split('.')[-1]
  filename = self.name + "." + ext
  return '/'.join(['album', self.artists.stage_name, filename])


class Album(models.Model):
  name = models.CharField(max_length=150)
  artists = models.ManyToManyField(Artist, through='ArtistAlbum', blank=True) #ForeignKey -> ManyToManyField & through: 여러 아티스트가 모일 경우 고려
    # black=True를 해줘야함.???
  image = models.ImageField(upload_to=get_album_image_path)
  description = models.TextField()
  release_at = models.DateTimeField(default=datetime.now) #released_date -> release_at : general & DateTimeField임을 표현
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
  type = models.CharField(max_length=2, choices=ALBUM_TYPE) #필드안에 choice를 넣을 수 있음 (검색, 공부!!)
  
  def __str__(self):
    return self.name # self.artist.stage_name제거 : 불러오는데 시간이 많이 소요됨 (*대안 self.artist_id)

class ArtistAlbum(models.Model):
  artist = models.ForeignKey(Artist, on_delete=models.PROTECT)
  album = models.ForeignKey(Album, on_delete=models.PROTECT)
  
  def __str__(self):
    return "artist" + str(self.artist_id) + "'s album" + str(self.album_id)
  
class Song(models.Model): # Music -> Song : Music은 Album을 포함할 수 있는 의미도 있어서
  album = models.ForeignKey(Album, on_delete=models.CASCADE, null=True)
  featuring = models.CharField(max_length=150, blank=True, null=True) # artist -> featuring : 피처링만 빼는게 좋음!
  title = models.CharField(max_length=300)
  is_title = models.BooleanField(default=False) # song에서는 의미있는 정보가 아니므로 through사용~, 의미가 있다면 둬도 괜찮음
  lyrics = models.TextField()
  description = models.TextField()
  genre = models.ManyToManyField(Genre)
  duration = models.TimeField() # length -> duration : 적절한 이름으로 변경!
  released_date = models.DateField()

  def __str__(self):
    if self.is_title:
      return self.title + " [title]" # self.album.name제거 : depth고려!
    return self.title
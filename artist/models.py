from django.db import models
from datetime import datetime
from music.models import Album


class Group(models.Model):
  name = models.CharField(max_length=150)
  debut_date = models.DateField(default=datetime.now)
  is_disbanded = models.BooleanField(default=False)
  
  def __str__(self):
    return self.name
  
class Artist(models.Model):
  stage_name = models.CharField(max_length=150)
  real_name = models.CharField(max_length=150)
  birthday = models.DateField(default=datetime.now) # birth -> birthday : data type에 의문을 갖을 수 있기 때문에
  group = models.ManyToManyField(Group, blank=True) # 한 아티스트가 여러 그룹에 속할 수 있으니 manytomanyfield 사용
  agency = models.CharField(max_length=150, blank=True, null=True)
  introduction = models.TextField()
  career = models.TextField(default='없음')
  debut_date = models.DateField(null=True, blank=True) # default=datetime.now -> null=True, blank=True : 생성 시각이 데뷔일이 아닐 수 있으므로 null이 가능하게 하도록
  
  def __str__(self):
    return self.stage_name

class ArtistAlbum(models.Model):
  artist = models.ForeignKey(Artist, on_delete=models.PROTECT)
  album = models.ForeignKey(Album, on_delete=models.PROTECT)
  
  def __str__(self):
    return "artist" + str(self.artist_id) + "'s album" + str(self.album_id)
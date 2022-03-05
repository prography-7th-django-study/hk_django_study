from django.db import models
from music.models import Song
from genre.models import Genre

def get_profile_image_path(self, filename):
  ext = filename.split('.')[-1]
  filename = self.nick_name + "." +ext
  return '/'.join(['profile', filename])


class User(models.Model):
  nickname = models.CharField(max_length=150, unique=True, # nick_name -> nickname : 원래 한 단어..
                               error_messages={'unique': 'Nickname is already in use.'})
  password = models.CharField(max_length=150) # max_length의 적절한 기준은 없지만 2^n or 2^n-1 정도로 잡음, 너무 딱 맞지만 않으면 괜찮음
  profile_image = models.ImageField(upload_to=get_profile_image_path, blank=True, null=True) 
  introduction = models.TextField(blank=True, null=True)
  joined_at = models.DateTimeField(auto_now_add=True)
  #followings = models.ManyToManyField("self", through='Follow', blank=True, null=True) : through 모델이 있으므로 필요없음!
  like_musics = models.ManyToManyField(Song, blank=True, related_name="users_like") # null=True제거 : ManyToManyField는 원래 허용
  like_genres = models.ManyToManyField(Genre, blank=True)
  like_playlists = models.ManyToManyField('PlayList', blank=True, related_name="users_like")
    # favortie은 가장 좋아하는 한 가지 느낌 이어서 가장 일반적인 like사용
  
  def __str__(self):
    return self.nickname
  
class PlayList(models.Model):
  name = models.CharField(max_length=50) # default 이름 필요 -> pk이용해서 V나 T에서 처리 => 생성시 receiver이용해서 이름 부여
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  created_at = models.DateField(auto_now_add=True)
  updated_at = models.DateField(auto_now=True) 
  musics = models.ManyToManyField(Song, blank=True)
  is_public = models.BooleanField(default=True) 
    
  def __str__(self):
    if self.is_public is True:
      return self.user_id + "의 공개 재생목록_" + str(self.pk) # self.user.nick_name -> self.user_id
    return self.user_id + "의 비공개 재생목록_" + str(self.pk)
  
class Follow(models.Model):
  followee = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followee') # user -> followee
  follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follower')
  follow_at = models.DateTimeField(auto_now_add=True)
  
  def __str__(self):
    return str(self.follower_id) + " is following " + str(self.followee_id) # followee.nick_name -> followee_id : depth줄이기
  
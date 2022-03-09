from django.db import models
from music.models import Song
from genre.models import Genre

def get_profile_image_path(self, filename):
    ext = filename.split('.')[-1]
    filename = self.nick_name + "." +ext
    return '/'.join(['profile', self.pk, filename])


class User(models.Model):
    nickname = models.CharField(max_length=150, unique=True,
                                error_messages={'unique': 'Nickname is already in use.'})
    password = models.CharField(max_length=150)
    profile_image = models.ImageField(upload_to=get_profile_image_path, blank=True, null=True) 
    introduction = models.TextField(blank=True, null=True)
    joined_at = models.DateTimeField(auto_now_add=True)
    followers = models.ManyToManyField("self", through='Relationship', blank=True) # relationship이 알아보기 어려워서 followers로 바꿈..
    like_musics = models.ManyToManyField(Song, blank=True, related_name="users_like")
    like_genres = models.ManyToManyField(Genre, blank=True)
    like_playlists = models.ManyToManyField('PlayList', blank=True, related_name="users_like")
    
    def __str__(self):
        return self.nickname
  
class PlayList(models.Model): #순환 import문제는 해결하고 앱으로 분리하는게 좋음
    name = models.CharField(max_length=50) # default 이름 필요 -> pk이용해서 V나 T에서 처리 => 생성시 receiver이용해서 이름 부여
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_playlists')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True) 
    musics = models.ManyToManyField(Song, blank=True)
    is_public = models.BooleanField(default=True) 
      
    def __str__(self):
        if self.is_public is True:
            return str(self.user_id) + "의 공개 재생목록_" + str(self.pk)
        return str(self.user_id) + "의 비공개 재생목록_" + str(self.pk)
  
class Relationship(models.Model):
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follower')
    follow_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.follower_id) + " is following " + str(self.following_id)
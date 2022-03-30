from django.db import models


class PlayList(models.Model):
    name = models.CharField(max_length=50) # default 이름 필요 -> pk이용해서 V나 T에서 처리 => 생성시 receiver이용해서 이름 부여
    user = models.ForeignKey('user.User', on_delete=models.CASCADE, related_name='user_playlists')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True) 
    musics = models.ManyToManyField('music.Song', blank=True)
    is_public = models.BooleanField(default=True) 
      
    def __str__(self):
        if self.is_public is True:
            return str(self.user_id) + "의 공개 재생목록_" + str(self.pk)
        return str(self.user_id) + "의 비공개 재생목록_" + str(self.pk)
    
    class Meta:
        ordering = ["id"]
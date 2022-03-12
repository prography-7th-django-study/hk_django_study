from django.db import models
from datetime import datetime

def get_artist_profile_image_path(self, filename):
    ext = filename.split('.')[-1]
    filename = self.nick_name + "." +ext
    return '/'.join(['artist','profile', self.pk, filename])


class Group(models.Model):
    name = models.CharField(max_length=150)
    debut_date = models.DateField(default=datetime.now)
    is_disbanded = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
  
class Artist(models.Model):
    profile_image = models.ImageField(upload_to=get_artist_profile_image_path, blank=True, null=True)
    stage_name = models.CharField(max_length=150)
    real_name = models.CharField(max_length=150)
    birthday = models.DateField(default=datetime.now)
    group = models.ManyToManyField(Group, blank=True)
    agency = models.CharField(max_length=150, blank=True, null=True)
    introduction = models.TextField()
    career = models.TextField(default='없음')
    debut_date = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return self.stage_name
from django.db import models


class Genre(models.Model):
  name = models.CharField(max_length=100) # genre -> name : Genre.name으로 접근하는것이 이해하기 좋음
  
  def __str__(self):
    return self.name
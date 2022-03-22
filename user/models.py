from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.contrib.auth.hashers import make_password
                                      

def get_profile_image_path(self, filename):
    ext = filename.split('.')[-1]
    filename = self.nick_name + "." +ext
    return '/'.join(['profile', self.pk, filename])

class UserManager(BaseUserManager): # use only password, last_login columns
    def _create_user(self, nickname, password, **extra_fields):
        if not nickname:
            raise ValueError("The given nickname must be set")
        user = self.model(nickname=nickname, **extra_fields)
        user.password = make_password(password) #hash화
        user.save(using=self._db)
        return user
    
    def create_user(self, nickname, password, **extra_fields):
        extra_fields.setdefault("is_admin", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(nickname, password, **extra_fields)

    # 내장된 함수는 그대로 사용하는게 좋음 (parameter, return)
    def create_superuser(self, nickname, password=None, **extra_fields):
        extra_fields.setdefault("is_admin", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_admin") is not True:
            raise ValueError("Superuser must have is_admin=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(nickname, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    # To make it easy to include Django’s permission framework into your own user class, Django provides PermissionsMixin. 
    # This is an abstract model you can include in the class hierarchy for your user model, 
    # giving you all the methods and database fields necessary to support Django’s permission model.
    nickname = models.CharField(max_length=150, unique=True,
                                error_messages={'unique': 'Nickname is already in use.'})
    # password = models.CharField(max_length=150) # abstractbaseuser에 정의되어있어서 필요없음.
    profile_image = models.ImageField(upload_to=get_profile_image_path, blank=True, null=True) 
    introduction = models.TextField(blank=True, null=True)
    joined_at = models.DateTimeField(auto_now_add=True)
    followers = models.ManyToManyField("self", through='Relationship', blank=True)
    favorite_musics = models.ManyToManyField('music.Song', blank=True, related_name="users_favorite")
    favorite_genres = models.ManyToManyField('genre.Genre', blank=True)
    favorite_playlists = models.ManyToManyField('playlist.PlayList', blank=True, related_name="users_favorite")
    
    # When a user no longer wishes to use our platform, they may try to delete
    # their account. That's a problem for us because the data we collect is
    # valuable to us and we don't want to delete it. We
    # will simply offer users a way to deactivate their account instead of
    # letting them delete it. That way they won't show up on the site anymore,
    # but we can still analyze the data.
    is_active = models.BooleanField(default=True) # required
    is_admin = models.BooleanField(default=False) # required
    
    # The `USERNAME_FIELD` property tells us which field we will use to log in.
    USERNAME_FIELD = 'nickname'
    REQUIRED_FIELDS = []
    
    # Tells Django that the UserManager class defined above should manage
    # objects of this type.
    objects = UserManager()
    
    def __str__(self):
        return self.nickname
    
    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
  
class Relationship(models.Model):
    following = models.ForeignKey('user.User', on_delete=models.CASCADE, related_name='following')
    follower = models.ForeignKey('user.User', on_delete=models.CASCADE, related_name='follower')
    follow_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.follower_id) + " is following " + str(self.following_id)
from re import A
from django.contrib import admin
from .models import User, PlayList, Follow
# Register your models here.
admin.site.register(User)
admin.site.register(PlayList)
admin.site.register(Follow)
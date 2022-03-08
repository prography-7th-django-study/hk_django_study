from re import A
from django.contrib import admin
from .models import User, PlayList, Relationship
# Register your models here.
admin.site.register(User)
admin.site.register(PlayList)
admin.site.register(Relationship)
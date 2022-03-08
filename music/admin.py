from django.contrib import admin
from .models import Album, Song

admin.site.register(Song)
admin.site.register(Album)

# FK or ManyToManyField 입려하려고할 때
# class ArtistInline(admin.TabularInline):
#    model = Album.artists.through

# @admin.register(Album)
# class AlbumAdmin(admin.ModelAdmin):
#    inlines = [ArtistInline,]
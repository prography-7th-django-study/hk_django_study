from django.contrib import admin
from .models import Album, Song, ArtistAlbum

admin.site.register(Song)
admin.site.register(Album)
admin.site.register(ArtistAlbum)

# FK or ManyToManyField 입려하려고할 때
# class ArtistInline(admin.TabularInline):
#    model = Album.artists.through

# @admin.register(Album)
# class AlbumAdmin(admin.ModelAdmin):
#    inlines = [ArtistInline,]
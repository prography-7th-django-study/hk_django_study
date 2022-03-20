from rest_framework import serializers, permissions
from .models import Album, Song


# CustomizingFields   
class ArtistCustomizingField(serializers.RelatedField):
    def to_representation(self, value):
        return "Artist %d: %s" % (value.pk, value.stage_name)

# Serializers
class AlbumSerializer(serializers.ModelSerializer):
    artists = ArtistCustomizingField(many=True, read_only=True)
    class Meta:
        model = Album
        fields = ['id','name','artists','image','type']
    
class AlbumDetailSerializer(AlbumSerializer, serializers.ModelSerializer):
    release_at = serializers.DateTimeField(format="%Y/%m/%d %H:%M")
    songs = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='title'
    )
    class Meta(AlbumSerializer.Meta):
        model = Album
        fields = ['songs','description','release_at'] + AlbumSerializer.Meta.fields
   
class AlbumArtistSerializer(serializers.ModelSerializer):
    artists = ArtistCustomizingField(many=True, read_only=True)
    class Meta:
        model = Album
        fields = ['artists','image']
                   
class SongSerializer(serializers.ModelSerializer):
    duration = serializers.DateTimeField(format='%H:%M')
    class Meta:
        model = Song
        fields = ['id','title','featuring','is_title','duration']
        
class SongDetailSerializer(SongSerializer, serializers.ModelSerializer):
    album = AlbumArtistSerializer() # By default nested serializers are read-only.
    class Meta(SongSerializer.Meta):
        fields = ['lyrics','description','genre','released_date','album'] + SongSerializer.Meta.fields 
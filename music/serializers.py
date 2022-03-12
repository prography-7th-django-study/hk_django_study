from rest_framework import serializers
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
        fields = AlbumSerializer.Meta.fields + ['songs','description','release_at']
   
class AlbumArtistSerializer(serializers.ModelSerializer):
    artists = ArtistCustomizingField(many=True, read_only=True)
    class Meta:
        model = Album
        fields = ['artists','image']
                   
class SongSerializer(serializers.ModelSerializer):
    duration = serializers.DateTimeField(format='%H:%M')
    album = AlbumArtistSerializer()
    class Meta:
        model = Song
        fields = ['id','title','featuring','is_title','duration','album']
        
class SongDetailSerializer(SongSerializer, serializers.ModelSerializer):
    class Meta(SongSerializer.Meta):
        fields = SongSerializer.Meta.fields + ['lyrics','description','genre','released_date']
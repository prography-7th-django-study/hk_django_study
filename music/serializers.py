from rest_framework import serializers
from .models import *


class ChoiceCustomizingField(serializers.ModelSerializer):
    def to_representation(self, value):
        pass
      
class ArtistCustomizingField(serializers.ModelSerializer):
    def to_representation(self, value):
        return "%d : %s" % (value.pk, value.stage_name)
    
    class Meta:
        model = Artist
        fields = '__all__'

class AlbumSerializer(serializers.ModelSerializer):
    artists = ArtistCustomizingField(many=True)
    class Meta:
        model = Album
        fields = ['id','name','artists','image', 'type']
    
class AlbumDetailSerializer(serializers.ModelSerializer):
    release_at = serializers.DateTimeField(format="%Y/%m/%d %H:%M")
    class Meta:
        model = Album
        fields = ['id','name','artist','image','description','release_at','type']
    
class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = '__all__'
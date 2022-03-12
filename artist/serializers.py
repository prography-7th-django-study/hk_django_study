from rest_framework import serializers
from .models import Group, Artist
from music.models import Album
from music.serializers import AlbumSerializer # Nested relationships
  # If the field is used to represent a to-many relationship, you should add the many=True flag to the serializer field.

    
class GroupListSerializer(serializers.ModelSerializer):
  class Meta:
    model = Group
    fields = ['id','name'] 
    
class GroupDetailSerializer(GroupListSerializer, serializers.ModelSerializer):
  class Meta(GroupListSerializer.Meta):
    model = Group
    fields = ['debut_date','is_disbanded'] + GroupListSerializer.Meta.fields 
       
class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['id','profile_image','group','stage_name']
    
class ArtistDetailSerializer(ArtistSerializer, serializers.ModelSerializer):
    albums = AlbumSerializer(many=True, read_only=True)
    class Meta(ArtistSerializer.Meta):
        fields = ['albums',
                  'real_name',
                  'birthday',
                  'agency',
                  'introduction',
                  'career',
                  'debut_date'] + ArtistSerializer.Meta.fields
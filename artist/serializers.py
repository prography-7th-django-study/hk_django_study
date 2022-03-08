from rest_framework import serializers
from .models import Group, Artist
from music.serializers import AlbumSerializer # Nested relationships
  # If the field is used to represent a to-many relationship, you should add the many=True flag to the serializer field.

    
class GroupSerializer(serializers.ModelSerializer):
  class Meta:
    model = Group
    fields = '__all__'
    
class ArtistSerializer(serializers.ModelSerializer):
  albums = AlbumSerializer(many=True, read_only=True)
  # SlugRelatedField?? : FK로 연결된 애들 가져올 수 있음
  class Meta:
    model = Artist
    fields = '__all__'
from rest_framework import serializers
from .models import PlayList
from user.serializers import SongCustomizingField

      
class PlayListSerializer(serializers.ModelSerializer):  
    user_id = serializers.PrimaryKeyRelatedField(many=False, read_only=True) # represent the target of the relationship using its primary key.
    musics = SongCustomizingField(many=True, read_only=True) # music에 있는 song들을 'pk:title' 로 보여주기위한 customizing
    class Meta:
        model = PlayList
        fields = ['id','name','user_id','musics']
    
class PlayListDetailSerializer(PlayListSerializer, serializers.ModelSerializer):
    class Meta(PlayListSerializer.Meta):
        fields = PlayListSerializer.Meta.fields + ['created_at','updated_at']
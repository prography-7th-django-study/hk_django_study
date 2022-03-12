from rest_framework import serializers
'''
  Serializer 는 queryset 과 model instance 같은 것들을 쉽게 JSON 또는 XML 의 데이터 형태로 렌더링 할 수 있게 해준다.
  Form 과 유사하게 데이터의 유효성 검사 및 데이터베이스로 저장한다.
'''
from .models import PlayList, User, Relationship


# CustomizingFields  
class PlayListCustomizingField(serializers.RelatedField):
    def to_representation(self, value):
        return "PlayList %d of %s" % (value.pk, value.name)
      
class SongCustomizingField(serializers.RelatedField): # music과 song이 뒤섞인 느낌..
    def to_representation(self, value):
        if value.is_title:
            return "Song %d: %s [title]" % (value.pk, value.title)
        else:
            return "Song %d: %s" % (value.pk, value.title)
      
class GenreCustomizingField(serializers.RelatedField):
    def to_representation(self, value):
        return "Genre %d: %s" % (value.pk, value.name)
      
class RelationshipCustomizingField(serializers.RelatedField):
    def to_representation(self, value):
        return "%s" % (value.nickname)
     
# Serializers 
class UserListSerializer(serializers.ModelSerializer):
  class Meta:
      model = User
      fields = ['id','nickname','profile_image'] # 필드를 명확하게 밝히는게 중요
      
class UserDetailSerializer(serializers.ModelSerializer):
    joined_at = serializers.DateTimeField(format="%Y/%m/%d %H:%M")
    followers = RelationshipCustomizingField(many=True, read_only=True)
    like_musics = SongCustomizingField(many=True, read_only=True)
    like_genres = GenreCustomizingField(many=True, read_only=True)
    like_playlists = PlayListCustomizingField(many=True, read_only=True)
    class Meta:
        model = User
        fields = [
            'nickname',
            'profile_image',
            'introduction',
            'joined_at',
            'followers',
            'like_musics',
            'like_genres',
            'like_playlists'
        ]
        
class UserPasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','nickname','password']

class PlayListSerializer(serializers.ModelSerializer):  
    user_id = serializers.PrimaryKeyRelatedField(many=False, read_only=True) # represent the target of the relationship using its primary key.
    musics = SongCustomizingField(many=True, read_only=True) # music에 있는 song들을 'pk:title' 로 보여주기위한 customizing
    class Meta:
        model = PlayList
        fields = ['id','name','user_id','musics']
    
class PlayListDetailSerializer(PlayListSerializer, serializers.ModelSerializer):
    class Meta(PlayListSerializer.Meta):
        fields = PlayListSerializer.Meta.fields + ['created_at','updated_at']

class RelationshipSerializer(serializers.ModelSerializer):
    follow_at = serializers.DateTimeField(format="%Y/%m/%d %H:%M")
    class Meta:
        model = Relationship
        fields = ['following','follower','follow_at']
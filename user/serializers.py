from rest_framework import serializers
'''
  Serializer 는 queryset 과 model instance 같은 것들을 쉽게 JSON 또는 XML 의 데이터 형태로 렌더링 할 수 있게 해준다.
  Form 과 유사하게 데이터의 유효성 검사 및 데이터베이스로 저장한다.
'''
from .models import PlayList, User, Relationship


class PlayListCustomizingField(serializers.ModelSerializer):
    def to_representation(self, value):
        return "%d : %s's %s playlist" % (value.pk, value.user.pk, value.name)
      
class SongCustomizingField(serializers.ModelSerializer): # music과 song이 뒤섞인 느낌..
    def to_representation(self, value):
        return "%d : %s" % (value.pk, value.title)
      
class GenreCustomizingField(serializers.ModelSerializer):
    def to_representation(self, value):
        return "%d : %s" % (value.pk, value.name)
      
class RelationshipCustomizingField(serializers.ModelSerializer):
    def to_representation(self, value):
        return "%s" % (value.nickname)
      
class UserListSerializer(serializers.ModelSerializer):
  class Meta:
      model = User
      fields = ['id','nickname','profile_image'] # 필드를 명확하게 밝히는게 중요
    
class UserDetailSerializer(serializers.ModelSerializer):
    joined_at = serializers.DateTimeField(format="%Y/%m/%d %H:%M")
    followers = RelationshipCustomizingField(many=True)
    like_musics = SongCustomizingField(many=True)
    like_genres = GenreCustomizingField(many=True)
    like_playlists = PlayListCustomizingField(many=True)
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

class PlayListSerializer(serializers.ModelSerializer):  
    user_id = serializers.PrimaryKeyRelatedField(many=False, read_only=True) # represent the target of the relationship using its primary key.
    musics = SongCustomizingField(many=True) # music에 있는 song들을 'pk:title' 로 보여주기위한 customizing
    class Meta:
        model = PlayList
        fields = ['id','name','user_id','musics']
    
class PlayListDetailSerializer(serializers.ModelSerializer):
    user_id = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    musics = SongCustomizingField(many=True)
    class Meta:
        model = PlayList
        fields = ['id','name','user_id','created_at','updated_at','musics']

class RelationshipSerializer(serializers.ModelSerializer):
    follow_at = serializers.DateTimeField(format="%Y/%m/%d %H:%M")
    class Meta:
        model = Relationship
        fields = ['following','follower','follow_at']
from rest_framework import serializers
from .models import User, Relationship
# from rest_framework_jwt.settings import api_settings
# from rest_framework_simplejwt.tokens import RefreshToken
from user.models import User


# CustomizingFields  
class PlayListCustomizingField(serializers.RelatedField):
    def to_representation(self, value):
        return "PlayList %d of %s" % (value.pk, value.name)

class SongCustomizingField(serializers.RelatedField):
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
class UserLoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['nickname','password']
        
    def validate(self, data):
        nickname = data.get('nickname',None)
        user = User.objects.get(nickname=nickname)
        if user is None:
            return {
                'nickname':'None'
            }
        self.user = user
        return data
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','nickname','is_active','is_admin']

class UserListSerializer(serializers.ModelSerializer):
  class Meta:
      model = User
      fields = ['id','nickname','profile_image']
      
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

class RelationshipSerializer(serializers.ModelSerializer):
    follow_at = serializers.DateTimeField(format="%Y/%m/%d %H:%M")
    class Meta:
        model = Relationship
        fields = ['following','follower','follow_at']
        
class RegistrationSerializer(serializers.ModelSerializer):
    """Serializers registration requests and creates a new user."""

    # Ensure passwords are at least 8 characters long, no longer than 128
    # characters, and can not be read by the client.
    password = serializers.CharField(
        max_length=128,
        write_only=True
    )

    # The client should not be able to send a token along with a registration
    # request. Making `token` read-only handles that for us.
    token = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = User
        # List all of the fields that could possibly be included in a request
        # or response, including fields specified explicitly above.
        fields = ['nickname', 'password', 'token']

    def create(self, validated_data):
        # Use the `create_user` method we wrote earlier to create a new user.
        print(validated_data)
        return User.objects.create_user(**validated_data)
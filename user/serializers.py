from rest_framework import serializers
# Serializer 는 queryset 과 model instance 같은 것들을 쉽게 JSON 또는 XML 의 데이터 형태로 렌더링 할 수 있게 해준다
# Form 과 유사하게 데이터의 유효성검사 및 데이터베이스로 저장한다
from .models import PlayList, User, Relationship


class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = '__all__'
    extra_fields = ['playlists'] # 왜 안보이지...
    
class PlayListSerializer(serializers.ModelSerializer):  
  user_id = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    # represent the target of the relationship using its primary key.
  class Meta:
    model = PlayList
    fields = '__all__'
    
class RelationshipSerializer(serializers.ModelSerializer):
  class Meta:
    model = Relationship
    fields = '__all__'
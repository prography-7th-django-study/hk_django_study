# mixins 사용시
from .serializers import GroupSerializer, ArtistSerializer
from .models import Group, Artist
from music.serializers import AlbumSerializer
from rest_framework import mixins
from rest_framework import generics #provide commonly needed behaviour

# generics 사용시
from rest_framework import generics
from .models import *
from .serializers import *

# Mixin 상속
# APIView는 CRUD를 직접 처리한다. 이 부분은 많이 사용되므로 중복이 발생한다.
# 따라서 rest_framework.mixins에 이것들을 미리 구현해놨다.
# queryset 과 serializer_class 를 지정해주기만 하면 나머지는 상속받은 Mixin 과 연결해주기만 하면 된다.

# CBV - Mixin - Group
class GroupPostListMixins(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
  queryset = Group.objects.all()
  serializer_class = GroupSerializer
  
  def get(self, request, *args, **kwargs):
    return self.list(request)
  
  def post(self, request, *args, **kwargs):
    return self.create(request)
  
class GroupDetailMixins(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
  queryset = Group.objects.all()
  serializer_class = GroupSerializer
  
  def get(self, request, *args, **kwargs):
    return self.retrieve(request)
  
  def put(self, request, *args, **kwargs):
    return self.update(request, *args, **kwargs)
      
  def delete(self, request, *args, **kwargs):
    return self.delete(request, *args, **kwargs)

## generics APIView ##
# Mixin 을 상속함으로서 반복되는 내용을 많이 줄일 수 있었습니다. 
# 하지만 여러 개를 상속해야 하다보니 가독성이 떨어집니다. 
# 다행히도 rest_framework 에서는 저들을 상속한 새로운 클래스를 정의해놨습니다.

# CBV - Generics - Artist
class ArtistListGenericAPIView(generics.ListCreateAPIView):
  queryset = Artist.objects.all()
  serializer_class = ArtistSerializer
  
class ArtistDetailGenericAPIView(generics.RetrieveUpdateDestroyAPIView):
  queryset = Artist.objects.all()
  serializer_class = ArtistSerializer
from .models import Group, Artist
from rest_framework import viewsets, generics # provide commonly needed behaviour
from .models import Artist, Group
from .serializers import *


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
  
    def get_serializer_class(self):
        if self.action == 'list':
            return GroupListSerializer
        else:
            return GroupDetailSerializer

class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    
    def get_serializer_class(self):
        if self.action == 'list':
            return ArtistSerializer
        else:
            return ArtistDetailSerializer
  
'''
>> Mixin 상속
APIView는 CRUD를 직접 처리한다. 이 부분은 많이 사용되므로 중복이 발생한다.
따라서 rest_framework.mixins에 이것들을 미리 구현해놨다.
queryset 과 serializer_class 를 지정해주기만 하면 나머지는 상속받은 Mixin 과 연결해주기만 하면 된다.

>> generics APIView
Generics -> 최소 기능 생성
Mixin 을 상속함으로서 반복되는 내용을 많이 줄일 수 있었습니다. 
하지만 여러 개를 상속해야 하다보니 가독성이 떨어집니다. 
다행히도 rest_framework 에서는 저들을 상속한 새로운 클래스를 정의해놨습니다.
'''
from .models import Group, Artist
from rest_framework import viewsets
from .models import Artist, Group
from .serializers import *


class GroupViewSet(viewsets.ModelViewSet):
    '''
    # 그룹인 가수 조회, 상세조회 API
    ---
    ## URL
    ## 조회
        '/groups'
    ## 상세조회
        '/groups/{id}
    '''
    queryset = Group.objects.all()
  
    def get_serializer_class(self):
        if self.action == 'list':
            return GroupListSerializer
        else:
            return GroupDetailSerializer

class ArtistViewSet(viewsets.ModelViewSet):
    '''
    # 그룹이 아닌 가수 한 명 한 명을 조회, 상세조회할 수 있는 API
    ---
    ## URL
    ## 가수 조회
        '/artists'
    ## 가수 상세 조회
        '/artists/{id}'
    '''
    queryset = Artist.objects.all()
    
    def get_serializer_class(self):
        if self.action == 'list':
            return ArtistSerializer
        else:
            return ArtistDetailSerializer
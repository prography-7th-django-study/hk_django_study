from django.shortcuts import get_object_or_404
from .models import Album, Song
from .serializers import AlbumDetailSerializer, AlbumSerializer, SongSerializer, SongDetailSerializer
from rest_framework import viewsets
from rest_framework.response import Response

'''
ViewSet
-일반적인 CBV 가 아니기 때문에 as_view 를 통해서 뷰를 만들지 않고 router를 사용
-as_view 를 사용하지 않는 이유는 ViewSet 은 하나의 뷰가 아닌 set, 여러 개의 뷰를 만들 수 있는 확장된 CBV이기 때문
-ModelViewSet 이 ReadOnlyModelViewSet 의 기능들을 함축
'''

class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    
    def get_serializer_class(self): # generics.GenericAPIView에 정의되어있음.
        if self.action == 'list':
            return AlbumSerializer
        else:
            return AlbumDetailSerializer

class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    
    def get_serializer_class(self):
        if self.action == 'list':
            return SongSerializer
        else:
            return SongDetailSerializer

'''
SongViewSet의 Router역할이 아래와같이 http method별로 함수 실행하는 것
songs = SongViewSet.as_view({
  'get': 'list',
  'post': 'create',
})

songs_detail = SongViewSet.as_view({
  'get': 'retrieve',
  'put': 'update',
  'patch': 'partial_update',
  'delete': 'destroy',
})
'''
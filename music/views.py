from django.shortcuts import render
from .models import Album, Song
from .serializers import AlbumSerializer, SongSerializer
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet  

# ViewSet
# 일반적인 CBV 가 아니기 때문에 as_view 를 통해서 뷰를 만들지 않고 router를 사용했습니다.
# as_view 를 사용하지 않는 이유는 ViewSet 은 하나의 뷰가 아닌 set, 여러 개의 뷰를 만들 수 있는 확장된 CBV이기 때문입니다.
# ModelViewSet 이 ReadOnlyModelViewSet 의 기능들을 함축

class AlbumViewSet(viewsets.ModelViewSet):
  queryset = Album.objects.all()
  serializer_class = AlbumSerializer    
  
class SongViewSet(ModelViewSet):
  queryset = Song.objects.all()
  serializer_class = SongSerializer   

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
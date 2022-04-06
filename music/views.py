from .models import Album, Song
from .serializers import AlbumDetailSerializer, AlbumSerializer, SongSerializer, SongDetailSerializer
from rest_framework import viewsets


class AlbumViewSet(viewsets.ModelViewSet):
    '''
    # 음악 앨범을 조회, 상세 조회 하는 API
    ---
    ## URL
    ## 음악 앨범 조회
        '/alnums'
    ## 음악 앨범 상세 조회
    '''
    queryset = Album.objects.all()
    
    def get_serializer_class(self):
        if self.action == 'list':
            return AlbumSerializer
        else:
            return AlbumDetailSerializer

class SongViewSet(viewsets.ModelViewSet):
    '''
    # 음악을 조회, 상세 조회 하는 API
    ---
    ## URL
    ## 음악 조회
        '/songs'
    ## 음악 상세 조회
        '/songs/{id}'
    '''
    queryset = Song.objects.all()
    
    def get_serializer_class(self):
        if self.action == 'list':
            return SongSerializer
        else:
            return SongDetailSerializer  
from .models import Album, Song
from .serializers import AlbumDetailSerializer, AlbumSerializer, SongSerializer, SongDetailSerializer
from rest_framework import viewsets


class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    
    def get_serializer_class(self):
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
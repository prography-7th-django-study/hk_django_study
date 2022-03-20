from .models import Group, Artist
from rest_framework import viewsets
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
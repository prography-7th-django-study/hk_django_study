from rest_framework import viewsets
from .models import PlayList
from .serializers import PlayListSerializer, PlayListDetailSerializer


class PlayListViewSet(viewsets.ModelViewSet):
    queryset = PlayList.objects.all()
    ordering_fields = ['id']
    def get_serializer_class(self):
        if self.action == 'list':
            return PlayListSerializer
        else:
            return PlayListDetailSerializer
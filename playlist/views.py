from rest_framework import viewsets
from .models import PlayList
from .serializers import PlayListSerializer, PlayListDetailSerializer


class PlayListViewSet(viewsets.ModelViewSet):
    '''
    # 사용자 재생목록을 조회, 상세 조회 하는 API
    ---
    ## URL
    ## 공개 재생목록 조회
        '/playlists'
    ## 재생목록 상세 조회
        '/playlists/{id}'
    '''
    queryset = PlayList.objects.all()
    ordering_fields = ['id']
    def get_serializer_class(self):
        if self.action == 'list':
            return PlayListSerializer
        else:
            return PlayListDetailSerializer
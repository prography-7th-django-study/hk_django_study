from .models import Genre
from .serializers import GenreSerializer
from rest_framework import viewsets


class GenreViewSet(viewsets.ModelViewSet):
    '''
    # 장르 조회, 상세조회 API
    ---
    ## URL
    ## 조회
        '/genres'
    ## 상세조회
        '/genres/{id}'
    '''
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

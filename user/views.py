from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from .models import PlayList, Relationship, User
from .serializers import *


class UserViewSet(viewsets.ViewSet):
    def list(self, request):
        queryet = User.objects.all()
        serializer = UserListSerializer(queryet, many=True)
        return Response(serializer.data)
      
    def retrieve(self, request, pk=None): # the DefaultRouter will configure detail actions to contain pk in their URL patterns.
        queryset = User.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = UserDetailSerializer(user)
        return Response(serializer.data)
        
class PlayListViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = PlayList.objects.all()
        serializer = PlayListSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = PlayList.objects.all()
        playlist = get_object_or_404(queryset, pk=pk)
        serializer = PlayListDetailSerializer(playlist)
        return Response(serializer.data)
      
class RelationshipViewSet(viewsets.ModelViewSet):
    queryset = Relationship.objects.all()
    serializer_class = RelationshipSerializer


'''
FBV 사용은 거의 안함. ping보내는 용도정도, 직관적인 것 구현하는 정도, View를 사용하면 틀이 커지니까

데코레이터는 함수의 시작과 끝의 동작을 해줌. 
@api_view(['GET','POST']) # DRF에서 사용하기 위해 필요, 처음에 허용 메소드를 확인하기위해서(문지기~) = wrapping해준다고 함

HttpResponse vs JsonResponse 
1. HttpResponse(data, content_type) 
  - response를 반환하는 가장 기본적인 함수
  - 주로 html를 반환
2. JsonResponse(data, encoder=DjangoJSONEncoder, safe=True, json_dumps_params=None, **kwargs)
  - HttpResponse의 subclass로, JSON-encoded response를 생성 할 수 있게 해 줌
  - 대부분의 기능은 superclass에서 상속받음
  - 디폴트 Content-type 헤더는 application/json
  - data는 반드시 dictionary 객체여야함
  - encoder는 데이터를 serialize할 때 이용됨
  - json_dumps_params는 json.dumps()에 전달할 딕셔너리의 keyword arguments
   JsonResponse는 response를 커스터마이징 하여 전달하고 싶을때, http status code에 더하여 메세지를 입력해서 전달할 수 있다.
  이 메세지는 프론트엔드 개발자와 협의하여 약속된 메시지를 던진다. 만약 딱히 전달할 메시지가 없고, status code만 전달한다면 HttpResponse를 사용하면 된다.
  메세지를 입력할 때는 보안 이슈가 있기 때문에 너무 자세히 적지 않는 것이 좋다.
'''
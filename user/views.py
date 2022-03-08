from django.shortcuts import get_object_or_404
from rest_framework import status, mixins
from rest_framework.response import Response # HTTPResponse는 광범위한 response, rest_api쓸때는 Response사용하면 됨
from rest_framework.decorators import api_view
  # Decorator that converts a function-based view into an APIView subclass.
  # Takes a list of allowed methods for the view as an argument.
from .models import PlayList, Relationship, User
from .serializers import PlayListSerializer, RelationshipSerializer, UserSerializer


# 복잡한 코드가 여러 함수에 중복적으로 들어가야할 경우 decorator 를 통해서 단순화 해 줄 수 있다.
# -> 사실 잘 못알아듣겠음... 예시가 이해불가,,
#https://ssungkang.tistory.com/entry/python-%EC%9E%A5%EC%8B%9D%EC%9E%90-%EB%8D%B0%EC%BD%94%EB%A0%88%EC%9D%B4%ED%84%B0decorator-%EB%A5%BC-%EC%95%8C%EC%95%84%EB%B3%B4%EC%9E%90
# FBV - User
@api_view(['GET','POST'])
def user_list(request): # R, C
  if request.method == 'GET':
    users = User.objects.all()
    serializers = UserSerializer(users, many=True)
    return Response(serializers.data)
  else:
    serializers = UserSerializer(data=request.data)
    if serializers.is_valid():
      serializers.save()
      return Response(serializers.data, status=201) # 성공적 추가
    return Response(serializers.data, status=400) # 클라이언트 요청 에러
  
@api_view(['GET','PUT','DELETE'])
def user_detail(request, pk): # R-detail, D, U
  user = get_object_or_404(User, pk=pk)
  if request.method == 'GET':
    serializers = UserSerializer(user)
    return Response(serializers.data)
  elif request.method == 'PUT':
    serializers = UserSerializer(user, data=request.data)
    if serializers.is_valid():
      serializers.save()
      return Response(serializers.data, status=201)
    return Response(serializers.error, status=status.HTTP_400_BAD_REQUEST) 
  else:
    user.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

# FBV - PlayList    
@api_view(['GET','POST'])
def play_list(request):
  if request.method == 'GET':
    play_lists = PlayList.objects.filter(is_public=True) # R - filtered
    serializers = PlayListSerializer(play_lists, many=True)
    return Response(serializers.data)
  else:
    serializers = PlayListSerializer(data=request.data)
    if serializers.is_valid():
      serializers.save()
      return Response(serializers.data, status=201)
    return Response(serializers.data, status=400) 
  
@api_view(['GET','PUT','DELETE'])
def play_list_detail(request, pk): # R -detail
  play_list = get_object_or_404(PlayList.objects.filter(is_public=True), pk=pk)
  if request.method == 'GET':
    serializers = PlayListSerializer(play_list)
    return Response(serializers.data)
  elif request.method == 'PUT': # U
    serializers = PlayListSerializer(play_list, data=request.data)
    if serializers.is_valid():
      serializers.save()
      return Response(serializers.data, status=201)
    return Response(serializers.error, status=status.HTTP_400_BAD_REQUEST) 
  else:
    play_list.delete() # D
    return Response(status=status.HTTP_204_NO_CONTENT)
  
# FBV - Relationship    
@api_view(['GET','POST'])
def relationship(request):
  if request.method == 'GET': # R
    relationships = Relationship.objects.all()
    serializers = RelationshipSerializer(relationships, many=True)
    return Response(serializers.data)
  else:
    serializers = RelationshipSerializer(data=request.data) # C
    if serializers.is_valid():
      serializers.save()
      return Response(serializers.data, status=201)
    return Response(serializers.data, status=400) 
  
@api_view(['GET','PUT','DELETE'])
def relationship_detail(request, pk):
  relationships = get_object_or_404(Relationship, pk=pk)
  if request.method == 'GET':
    serializers = RelationshipSerializer(relationships)
    return Response(serializers.data)
  elif request.method == 'PUT':
    serializers = RelationshipSerializer(relationships, data=request.data)
    if serializers.is_valid():
      serializers.save()
      return Response(serializers.data, status=201)
    return Response(serializers.error, status=status.HTTP_400_BAD_REQUEST) 
  else:
    play_list.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
  

# HttpResponse vs Render vs JsonResponse 
# 1. HttpResponse(data, content_type) 
  # - response를 반환하는 가장 기본적인 함수
  # - 주로 html를 반환
# 2. render(request(필수), template_name(필수), context=None, content_type=None, status=None, using=None) 
  # - httpRespose 객체를 반환하는 함수로 template을 context와 엮어 httpResponse로 쉽게 반환해 주는 함수
# 3. JsonResponse(data, encoder=DjangoJSONEncoder, safe=True, json_dumps_params=None, **kwargs)
  # - HttpResponse의 subclass로, JSON-encoded response를 생성 할 수 있게 해 줌
  # - 대부분의 기능은 superclass에서 상속받음
  # - 디폴트 Content-type 헤더는 application/json
  # - data는 반드시 dictionary 객체여야함
  # - encoder는 데이터를 serialize할 때 이용됨
  # - json_dumps_params는 json.dumps()에 전달할 딕셔너리의 keyword arguments
  #  JsonResponse는 response를 커스터마이징 하여 전달하고 싶을때, http status code에 더하여 메세지를 입력해서 전달할 수 있다.
  # 이 메세지는 프론트엔드 개발자와 협의하여 약속된 메시지를 던진다. 만약 딱히 전달할 메시지가 없고, status code만 전달한다면 HttpResponse를 사용하면 된다.
  # 메세지를 입력할 때는 보안 이슈가 있기 때문에 너무 자세히 적지 않는 것이 좋다.
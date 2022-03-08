from rest_framework.views import APIView
from .models import Genre
from .serializers import GenreSerializer
from rest_framework.response import Response # HTTPResponse는 광범위한 response, rest_api쓸때는 Response사용하면 됨
from django.shortcuts import get_object_or_404
from rest_framework import status

# 클래스형(CBV) 뷰의 장점 #
# 1. 메소드에 따른 처리를 메소드 명으로 구분하여 if문 없는 깔끔한 코드
# 2. 다중 상속과 같은 객체 지향 기술이 가능하여 코드의 재사용성이나 개발 생산성을 높여줌

# APIView vs ViewSet #
# 1. ViewSet은 반복되는 로직을 하나의 클래스로 결합할 수 있다. queryset을 단 한번만 정의하면 된다
# 2. ViewSet은 Router를 사용함으로써 URL설정을 다룰 필요가 없다.
# 3. APIView의 경우 CURD 로직을 각각 작성해야한다.

# Genre
class GenreListAPIView(APIView): # R - list
  def get(self, request):
    genre_queryset = Genre.objects.all()
    serializer = GenreSerializer(genre_queryset, many=True)
    return Response(serializer.data)
 
class GenrePostAPIView(APIView): # C                               
  def post(self, request):
    serializer = GenreSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)
  
class GenreDetailAPIView(APIView): # R - detail
  def get_object(self, pk):
    return get_object_or_404(Genre, pk=pk)
    
  def get(self, request, pk, format=None):
    user = self.get_object(pk)
    serializer = GenreSerializer(user)
    return Response(serializer.data)
  
  def delete(self, request, pk): # D
    user = self.get_object(pk)
    user.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
 
class GenreUpdateAPIView(APIView): # U
  def get_object(self, pk):
    return get_object_or_404(Genre, pk=pk)
    
  def get(self, request, pk, format=None):
    user = self.get_object(pk)
    serializer = GenreSerializer(user)
    return Response(serializer.data)
  
  def put(self, request, pk):
    user = self.get_object(pk)
    serializer = GenreSerializer(user, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# APIView vs ViewSet #
# 1. ViewSet은 반복되는 로직을 하나의 클래스로 결합할 수 있다. queryset을 단 한번만 정의하면 된다
# 2. ViewSet은 Router를 사용함으로써 URL설정을 다룰 필요가 없다.
# 3. APIView의 경우 CURD 로직을 각각 작성해야한다.

# HTTPResponse vs Response
# REST framework provides an APIView class, which subclasses Django's View class.
# APIView classes are different from regular View classes in the following ways:
  # Requests passed to the handler methods will be REST framework's Request instances, not Django's HttpRequest instances.
  # Handler methods may return REST framework's Response, instead of Django's HttpResponse. The view will manage content negotiation and setting the correct renderer on the response.

# !! DRY !!
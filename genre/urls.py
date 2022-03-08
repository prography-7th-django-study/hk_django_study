from django.urls import path
from .views import *

app_name = 'genre'

urlpatterns = [
  # CBV - Genre CRUD
  path('genres', GenreListAPIView.as_view()), #클래스형 뷰는 클래스로 진입하기 위한 진입 메소드를 제공하는데, 이것이 as_view()메소드다.
  path('genres/post', GenrePostAPIView.as_view()),
  path('genres/<int:pk>/detail', GenreDetailAPIView.as_view()),
  path('genres/<int:pk>/update', GenreUpdateAPIView.as_view()),
]

## as_view() ##
	#1. as_view() 메소드에서 클래스의 인스턴스 생성
	#2. 생성된 인스턴스의 dispatch() 메소드를 호출
	#3. dispatch() 메소드는 요청을 검사해서 HTTP의 메소드(GET, POST)를 알아냄
	#4-1. 인스턴스 내에 해당 이름을 갖는 메소드로 요청을 중계
	#4-2. 해당 메소드가 정의되어 있지 않으면, HttpResponseNotAllowd 예외를 발생시킴
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

app_name = 'genre'

router = DefaultRouter() # create router
router.register(r'genres', GenreViewSet) # register viewset with router

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),  
]

# GenreView.as_view() : 클래스형 뷰는 클래스로 진입하기 위한 진입 메소드를 제공하는데, 이것이 as_view()메소드다.
## as_view() ##
	#1. as_view() 메소드에서 클래스의 인스턴스 생성
	#2. 생성된 인스턴스의 dispatch() 메소드를 호출
	#3. dispatch() 메소드는 요청을 검사해서 HTTP의 메소드(GET, POST)를 알아냄
	#4-1. 인스턴스 내에 해당 이름을 갖는 메소드로 요청을 중계
	#4-2. 해당 메소드가 정의되어 있지 않으면, HttpResponseNotAllowd 예외를 발생시킴
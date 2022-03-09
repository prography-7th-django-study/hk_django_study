from .models import Genre
from .serializers import GenreSerializer
from rest_framework import viewsets

# 클래스형(CBV) 뷰의 장점 #
# 1. 메소드에 따른 처리를 메소드 명으로 구분하여 if문 없는 깔끔한 코드
# 2. 다중 상속과 같은 객체 지향 기술이 가능하여 코드의 재사용성이나 개발 생산성을 높여줌

# APIView vs ViewSet #
# 1. ViewSet은 반복되는 로직을 하나의 클래스로 결합할 수 있다. queryset을 단 한번만 정의하면 된다.
# 2. ViewSet은 Router를 사용함으로써 URL설정을 다룰 필요가 없다.
# 3. APIView의 경우 CURD 로직을 각각 작성해야한다.

# Genre
class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
# dispatch method구분해서 처리 -> router 구현 필수
  
# patch?? : 엄격한 관리에 필요
# 일부 필드만 수정할 때 나머지는 null이 들어가버리니까 patch필요

# HTTPResponse vs Response
# REST framework provides an APIView class, which subclasses Django's View class.
# APIView classes are different from regular View classes in the following ways:
  # Requests passed to the handler methods will be REST framework's Request instances, not Django's HttpRequest instances.
  # Handler methods may return REST framework's Response, instead of Django's HttpResponse. The view will manage content negotiation and setting the correct renderer on the response.

# !! DRY !!
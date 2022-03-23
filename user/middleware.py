from .models import User
from django.http import JsonResponse
from django.core.exceptions import PermissionDenied
from .jwt import decode_jwt
from jwt.exceptions import ExpiredSignatureError
from http import HTTPStatus
from rest_framework.permissions import SAFE_METHODS

class JsonWebTokenMiddleWare(object):
  
    def __init__(self, get_response):
        self.get_response = get_response #장고에서 미들웨어를 호출할 때 넘겨주는 하나의 함수이며, view이거나 다른 미들웨어 일 수 있다
        
    def __call__(self, request): 
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        try:
            # 토큰을 포함하지 않아도 되는 요청을 path를 이용해 분기
            if (
                request.path != "/signup"
                and request.path != "/login"
                and "admin" not in request.path
                and request.path != SAFE_METHODS
            ):
                headers = request.headers
                access_token = headers.get("Authorization", None)

                if not access_token:
                    raise PermissionDenied()

                payload = decode_jwt(access_token)

                nickname = payload.get("nickname", None)

                if not nickname:
                    raise PermissionDenied()

                User.objects.get(nickname=nickname)

            response = self.get_response(request)
            return response

        except (PermissionDenied, User.DoesNotExist):
            return JsonResponse(
                {"error": "Authorization Error"}, status=HTTPStatus.UNAUTHORIZED
            )
        except ExpiredSignatureError:
            return JsonResponse(
                {"error": "Expired token. Please log in again."},
                status=HTTPStatus.FORBIDDEN,
            )
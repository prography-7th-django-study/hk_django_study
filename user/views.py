from rest_framework import viewsets, status, permissions
from .models import Relationship, User
from .serializers import *
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from .serializers import RegistrationSerializer
from django.views.decorators.csrf import csrf_exempt
from http import HTTPStatus
from json import loads
from user.jwt import generate_access_token
from django.http import JsonResponse, HttpResponseNotAllowed
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.validators import ASCIIUsernameValidator
from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError



@csrf_exempt # csrf와 관련된 인증은 사용하지 않을 것이기 때문에 csrf인증을 사용하지 않음을 명시
@api_view(['POST'])
def login_view(request):
    data = {} # JsonResponse
    status = HTTPStatus.OK # 200
    
    try:
        print("login_view")
        if request.method == "POST": # 사용자가 로그인 정보 입력
            json_body = loads(request.body) # json문자열을 python객체로 변환 (json -> dict)
            nickname = json_body.get("nickname", None)
            password = json_body.get("password", None)

            if not nickname or not password:
                raise ValueError() # 입력값이 잘못됨

            user = User.objects.get(nickname=nickname)

            if not user.check_password(password):
                raise ValueError()

            data["access_token"] = generate_access_token(nickname)
            data["nickname"] = nickname

        else:
            return HttpResponseNotAllowed(["POST"])

    except (ValueError, User.DoesNotExist):
        # Login request validation exception
        data["error"] = "Invalid form. Please fill it out again."
        status = HTTPStatus.BAD_REQUEST # 400
        
    return Response(data, status=status)


@csrf_exempt
@api_view(['POST'])
def signup_view(request):
    data = {}
    status = HTTPStatus.CREATED
    print("signup view")
    try:
        if request.method == "POST":
            json_body = loads(request.body)

            nickname = json_body.get("nickname", None)
            password = json_body.get("password", None)
            password_confirm = json_body.get("passwordConfirm", None)

            if not nickname or not password or not password_confirm:
                raise ValueError()

            if password != password_confirm:
                raise ValueError()

            nickname_validator = ASCIIUsernameValidator(
                message="Please check the nickname condition."
            )

            nickname_validator(nickname)
            validate_password(password)

            user = User.objects.create(nickname=nickname)
            user.set_password(password)
            user.save()

            data["access_token"] = generate_access_token(nickname)
            data["nickname"] = nickname

        else:
            return HttpResponseNotAllowed(["POST"])

    except ValidationError as e:
        # Password validation exception
        data["error"] = e.messages
        status = HTTPStatus.BAD_REQUEST

    except IntegrityError:
        # Duplicate user name exception
        data["error"] = "Duplicate user name. Please use a different name."
        status = HTTPStatus.BAD_REQUEST

    except ValueError:
        # Invalid user request exception
        data["error"] = "Invalid form. Please fill it out again."
        status = HTTPStatus.BAD_REQUEST

    return Response(data, status=status)
    
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    
    def get_serializer_class(self):
        if self.action == 'list':
            return UserListSerializer
        else:
            return UserDetailSerializer
    
    @action(methods=['post'], detail=True, permission_classes=[permissions.IsAdminUser, permissions.IsAuthenticated])
    def set_password(self, request, pk, *args, **kwargs):
        user = self.get_object()
        serializer = UserPasswordSerializer(data=request.data)
        if serializer.is_valid():
            user.set_password(serializer.validated_data['password'])
            user.save()
            return Response(data={'status': 'password set'}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)    
      
class RelationshipViewSet(viewsets.ModelViewSet):
    queryset = Relationship.objects.all()
    serializer_class = RelationshipSerializer
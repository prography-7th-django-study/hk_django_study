from django.urls import path, include
from .views import RelationshipViewSet, UserViewSet, RegistrationAPIView
from rest_framework.routers import SimpleRouter

app_name = 'user'

router = SimpleRouter() # SimpleRouter vs DefaultRouter
router.register(r'relationships', RelationshipViewSet, basename='relationships')
router.register(r'users', UserViewSet, basename='users'),

urlpatterns = [
    path('', include(router.urls)), 
    path('register/', RegistrationAPIView.as_view()),
]
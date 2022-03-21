from django.urls import path, include
from .views import RelationshipViewSet, UserViewSet, login_view, signup_view
from rest_framework.routers import SimpleRouter

app_name = 'user'

router = SimpleRouter() # SimpleRouter vs DefaultRouter
router.register(r'relationships', RelationshipViewSet, basename='relationships')
router.register(r'users', UserViewSet, basename='users'),

urlpatterns = [
    path('', include(router.urls)), 
    path("login", login_view, name="login_view"),
    path("signup", signup_view, name="signup_view"),
]
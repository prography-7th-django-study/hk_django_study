from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('user.urls')),
    path('', include('genre.urls')),
    path('', include('artist.urls')),
    path('', include('music.urls')),
    # 프론트입장에서 앱 구조 알 필요 없기 때문에 앱 이름 사용할 필요 없음
]
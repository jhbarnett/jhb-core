from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
# router.register(r'users', UserViewSet)
# router.register(r'users', UserCreateViewSet)

urlpatterns = [
    path(r'v1/', include(router.urls)),
]

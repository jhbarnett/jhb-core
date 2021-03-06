from django.conf import settings
from django.urls import path, re_path, include, reverse_lazy
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic.base import RedirectView
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
# from .users.views import UserViewSet, UserCreateViewSet

router = DefaultRouter()
# router.register(r'users', UserViewSet)
# router.register(r'users', UserCreateViewSet)

urlpatterns = [
    path(r'v1/', include(router.urls)),
]

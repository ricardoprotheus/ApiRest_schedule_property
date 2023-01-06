from django.urls import path, include
from rest_framework import routers
from decouple import config

from . import views
from accounts.api.viewsets import User_viewsets

version_api = config('API_VERSION')

router = routers.DefaultRouter()
router.register(r'accounts', User_viewsets, basename='accounts')

urlpatterns = [
    path(version_api, include(router.urls)),
    path('', views.home, name='home'),
]
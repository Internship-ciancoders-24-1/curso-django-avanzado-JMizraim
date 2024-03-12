""" Users URLs"""

#Django
from django.urls import path, include
from cride.users.views import UserViewSet

#Django REST Framework
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'users', UserViewSet, basename='users')

urlpatterns = [
    path('', include(router.urls))
]
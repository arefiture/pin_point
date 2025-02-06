from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)

from api.views import TagViewSet, UserViewSet


api_v1 = DefaultRouter()
api_v1.register('tags', TagViewSet)
api_v1.register('users', UserViewSet, basename='users')

urlpatterns = [
    path('', include(api_v1.urls)),
    path(
        'auth/token/', TokenObtainPairView.as_view(),
        name='token_obtain_pair'
    ),
    path(
        'auth/token/refresh/', TokenRefreshView.as_view(),
        name='token_refresh'
    ),
]

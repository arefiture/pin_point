from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import (
    LoginView,
    LogoutView,
    RegisterViewSet,
    TagViewSet,
    UserViewSet
)


api_v1 = DefaultRouter()
api_v1.register('tags', TagViewSet)
api_v1.register('users', UserViewSet, basename='users')

urlpatterns = [
    path(
        'register/', RegisterViewSet.as_view({'post': 'create'}),
        name='register'
    ),
    path('login/', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),

    path('', include(api_v1.urls)),
]

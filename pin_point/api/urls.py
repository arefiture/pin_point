from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import TagViewSet


api_v1 = DefaultRouter()
api_v1.register('tags', TagViewSet)

urlpatterns = [
    path('', include(api_v1.urls)),
]

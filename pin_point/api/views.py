from rest_framework import viewsets

from api.serializers import (
    TagSerializer
)
from notes.models import (
    Tag
)


class TagViewSet(viewsets.ModelViewSet):
    """Вьюсет для тегов."""

    queryset = Tag.objects.all()
    serializer_class = TagSerializer


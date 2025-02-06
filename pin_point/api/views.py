from django.contrib.auth import get_user_model
from rest_framework import mixins, permissions, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from api.serializers import (
    RegisterSerializer, TagSerializer, UserProfileSerializer
)
from notes.models import (
    Tag
)

User = get_user_model()


class UserViewSet(
    mixins.CreateModelMixin,  # Регистрация
    viewsets.GenericViewSet
):
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny, ]

    def get_serializer_class(self):
        """Выбор сериалайзера в зависимости от методов и действий."""
        if self.action == 'create':  # Под регистрацию
            return RegisterSerializer
        return UserProfileSerializer

    def create(self, request, *args, **kwargs):
        """Регистрация пользователя."""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        refresh = RefreshToken.for_user(user)
        tokens = {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }

        return Response(tokens, status=status.HTTP_201_CREATED)

    @action(
        detail=False, methods=['get'],
        permission_classes=[permissions.IsAuthenticated]
    )
    def me(self, request):
        serializer = self.get_serializer(request.user)
        return Response(serializer.data)


class TagViewSet(viewsets.ModelViewSet):
    """Вьюсет для тегов."""

    queryset = Tag.objects.all()
    serializer_class = TagSerializer

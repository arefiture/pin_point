from django.contrib.auth import get_user_model
from rest_framework import mixins, permissions, status, views, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView

from api.serializers import (
    LoginSerializer, RegisterSerializer, TagSerializer, UserProfileSerializer
)
from notes.models import (
    Tag
)

User = get_user_model()


class RegisterViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """Только регистрация."""
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        refresh = RefreshToken.for_user(user)
        tokens = {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }

        return Response(tokens, status=status.HTTP_201_CREATED)


class LoginView(TokenObtainPairView):
    """Какстомная авторизация через получение токенов."""
    serializer_class = LoginSerializer


class LogoutView(views.APIView):
    """Логаут с удалением токенов."""
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()  # Добавляем refresh-токен в черный список
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_400_BAD_REQUEST
            )


class UserViewSet(viewsets.GenericViewSet):
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated, ]

    @action(detail=False, methods=['get'])
    def me(self, request):
        serializer = self.get_serializer(request.user)
        return Response(serializer.data)


class TagViewSet(viewsets.ModelViewSet):
    """Вьюсет для тегов."""

    queryset = Tag.objects.all()
    serializer_class = TagSerializer

from django.contrib.auth import get_user_model
from rest_framework import serializers, validators

from notes.models import Favorite, Note, NoteTags, Tag

User = get_user_model()  # Выделить сериалайзер для регистрации/авторизации/действий

# TODO: на каждый из сериалайзеров нужно выделить отдельные для CRUD


class RegisterSerializer(serializers.ModelSerializer):
    """Сериалайзер под регистрацию."""

    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    email = serializers.EmailField(
        required=True,
        validators=[validators.UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(write_only=True, required=True)
    confirm_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'username', 'email', 'password',
            'confirm_password'
        )

    def validate(self, attrs):
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError(
                {'password': 'Пароли не совпадают!'}
            )
        return attrs

    def create(self, validated_data: dict):
        validated_data.pop('confirm_password')
        password = validated_data.pop('password')
        user = User.objects.create(
            **validated_data
        )
        user.set_password(password)
        user.save()
        return user


class UserProfileSerializer(serializers.ModelSerializer):
    """Сериалайзер под профиль."""

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name')
        read_only_fields = ('id', 'username', 'email')


class TagSerializer(serializers.ModelSerializer):
    """Сериалайзер тегов."""
    # TODO: Возможно, стоит сделать поле только для чтения.

    class Meta:
        model = Tag
        fields = ['id', 'name', 'slug']


class NoteSerializer(serializers.ModelSerializer):
    """Сериалайзер заметок."""
    # TODO: здесь стоит выделить ссыль на автора, а также is_favorite
    class Meta:
        model = Note
        fields = [
            'id', 'title', 'content', 'created_at', 'updated_at',
            'author', 'is_archive'
        ]
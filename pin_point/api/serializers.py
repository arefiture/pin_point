from django.contrib.auth import get_user_model
from rest_framework import serializers

from notes.models import Favorite, Note, NoteTags, Tag

User = get_user_model() # Выделить сериалайзер для регистрации/авторизации/действий

# TODO: на каждый из сериалайзеров нужно выделить отдельные для CRUD


class TagSerializer(serializers.ModelSerializer):
    """Сериалайзер тегов."""

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
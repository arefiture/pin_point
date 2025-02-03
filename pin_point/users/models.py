from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.utils import timezone


class User(AbstractUser):
    """Кастомная модель пользователя."""
    username = models.CharField(
        verbose_name='Ник',
        max_length=150,
        unique=True,
        help_text=(
            'Обязательно. Максимум 150 символов. Только буквы, цифры и @/./+/-/_.'
        ),
        validators=[UnicodeUsernameValidator()],
        error_messages={
            'unique': "Уникальное имя пользователя (ник).",
        },
    )
    first_name = models.CharField(
        verbose_name='Имя',
        help_text='Имя пользователя.',
        max_length=150,
        blank=True,
    )
    last_name = models.CharField(
        verbose_name='Фамилия',
        help_text='Фамилия пользователя.',
        max_length=150,
        blank=True,
    )
    email = models.EmailField(
        verbose_name='Электронная почта',
        help_text='Введите незанятый электронный адрес.',
        unique=True,
        error_messages={
            'unique': "Уникальный адрес электронный почты.",
        }
    )
    is_staff = models.BooleanField(
        verbose_name='Является админом',
        default=False,
        help_text=(
            'Указывает, доступна ли панель администратора.'
        ),
    )
    is_active = models.BooleanField(
        verbose_name='Является активной УЗ',
        default=True,
        help_text=(
            'Указывает возможность авторизации под данной УЗ. '
            'Снемити галочку вместо удаления.'
        ),
    )
    date_joined = models.DateTimeField(
        verbose_name='Дата регистрации',
        default=timezone.now
    )
    last_login = models.DateTimeField(
        verbose_name='Дата последней авторизации',
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['username']

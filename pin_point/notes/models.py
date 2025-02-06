from django.contrib.auth import get_user_model
from django.db import models
from slugify import slugify

User = get_user_model()


class Tag(models.Model):
    """Теги."""
    name = models.CharField(
        verbose_name='Наименование',
        max_length=31,
        unique=True,
        help_text='Уникальное наименование тега.',
    )
    slug = models.SlugField(
        verbose_name='Код тега',
        max_length=31,
        unique=True,
        blank=True,  # Для генерации из функции
    )

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
        ordering = ['slug']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
            # TODO: предусмотреть уникальность при обновлении.
        super().save(*args, **kwargs)


class Note(models.Model):
    """Заметки."""
    title = models.CharField(
        verbose_name='Заголовок',
        max_length=127,
        help_text='Заголовок заметки (максимум 127 символов).',
    )
    content = models.TextField(
        verbose_name='Примечание',
        help_text='Содержимое заметки.',
    )
    created_at = models.DateTimeField(
        verbose_name='Дата создания',
        auto_now_add=True,
        help_text='Дата и время создания заметки.',
    )
    updated_at = models.DateTimeField(
        verbose_name='Дата обновления',
        blank=True,
        help_text='Дата и время обновления заметки.'
    )
    author = models.ForeignKey(
        to=User,
        verbose_name='Автор',
        on_delete=models.CASCADE,
        help_text='Автор заметки.',
    )
    is_archive = models.BooleanField(
        verbose_name='Является архивной записью',
        default=False,
        help_text='Отображается только в архиве.'
    )

    class Meta:
        verbose_name = 'Заметка'
        verbose_name_plural = 'Заметки'
        ordering = ['created_at', 'author']

    def save(self, *args, **kwargs):
        if self.pk:  # PK назначается при создании. В моменте он пуст.
            self.updated_at = models.DateTimeField.auto_now
        super().save(*args, **kwargs)


class NoteTags(models.Model):
    """Связующая между тегами и заметками (М-М)."""
    note = models.ForeignKey(
        to=Note,
        verbose_name='Заметка',
        on_delete=models.CASCADE,
    )
    tag = models.ForeignKey(
        to=Tag,
        verbose_name='Тег',
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = 'Связь заметки и тега'
        verbose_name_plural = 'Связи заметок и тегов'
        ordering = ['note', 'tag']
        constraints = [
            models.UniqueConstraint(
                fields=['note', 'tag'],
                name='unique_tag_for_note'
            ),
        ]


class Favorite(models.Model):
    """Избранные заметки."""
    user = models.ForeignKey(
        to=User,
        verbose_name='Пользователь',
        on_delete=models.CASCADE,
        help_text='Пользователь, добавивший заметку в избранное.'
    )
    note = models.ForeignKey(
        to=Note,
        verbose_name='Заметка',
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = 'Избранная заметка пользователя'
        verbose_name_plural = 'Избранные заметки пользователей'
        ordering = ['user', 'note']
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'note'],
                name='unique_favorite_note_for_user'
            ),
        ]

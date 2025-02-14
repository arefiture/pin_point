# Generated by Django 3.2.16 on 2025-02-03 15:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Избранная заметка пользователя',
                'verbose_name_plural': 'Избранные заметки пользователей',
                'ordering': ['user', 'note'],
            },
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Заголовок заметки (максимум 127 символов).', max_length=127, verbose_name='Заголовок')),
                ('content', models.TextField(help_text='Содержимое заметки.', verbose_name='Примечание')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Дата и время создания заметки.', verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(blank=True, help_text='Дата и время обновления заметки.', verbose_name='Дата обновления')),
                ('is_archive', models.BooleanField(default=False, help_text='Отображается только в архиве.', verbose_name='Является архивной записью')),
            ],
            options={
                'verbose_name': 'Заметка',
                'verbose_name_plural': 'Заметки',
                'ordering': ['created_at', 'author'],
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Уникальное наименование тега.', max_length=31, unique=True, verbose_name='Наименование')),
                ('slug', models.SlugField(blank=True, max_length=31, unique=True, verbose_name='Код тега')),
            ],
            options={
                'verbose_name': 'Тег',
                'verbose_name_plural': 'Теги',
                'ordering': ['slug'],
            },
        ),
        migrations.CreateModel(
            name='NoteTags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notes.note', verbose_name='Заметка')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notes.tag', verbose_name='Тег')),
            ],
            options={
                'verbose_name': 'Связь заметки и тега',
                'verbose_name_plural': 'Связи заметок и тегов',
                'ordering': ['note', 'tag'],
            },
        ),
    ]

# Generated by Django 3.2.16 on 2025-02-03 15:48

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'Уникальное имя пользователя (ник).'}, help_text='Обязательно. Максимум 150 символов. Только буквы, цифры и @/./+/-/_.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='Ник')),
                ('first_name', models.CharField(blank=True, help_text='Имя пользователя.', max_length=150, verbose_name='Имя')),
                ('last_name', models.CharField(blank=True, help_text='Фамилия пользователя.', max_length=150, verbose_name='Фамилия')),
                ('email', models.EmailField(error_messages={'unique': 'Уникальный адрес электронный почты.'}, help_text='Введите незанятый электронный адрес.', max_length=254, unique=True, verbose_name='Электронная почта')),
                ('is_staff', models.BooleanField(default=False, help_text='Указывает, доступна ли панель администратора.', verbose_name='Является админом')),
                ('is_active', models.BooleanField(default=True, help_text='Указывает возможность авторизации под данной УЗ. Снемити галочку вместо удаления.', verbose_name='Является активной УЗ')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата регистрации')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='Дата последней авторизации')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
                'ordering': ['username'],
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]

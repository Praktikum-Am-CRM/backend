from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models


class Manager(AbstractUser):
    first_name = models.CharField(max_length=255, verbose_name='Имя')
    last_name = models.CharField(max_length=255, verbose_name='Фамилия')
    email = models.EmailField(unique=True, db_index=True)
    profession = models.CharField(
        max_length=255, verbose_name='Специальность', null=True, blank=True
    )
    middle_name = models.CharField(
        max_length=255, verbose_name='Отчество', null=True, blank=True
    )
    username = models.CharField(
        'Имя пользователя',
        max_length=150,
        unique=True,
        validators=(UnicodeUsernameValidator,),
    )
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = (
        'username',
        'first_name',
        'last_name',
    )

    def __str__(self):
        return f'{self.last_name} {self.first_name} {self.middle_name}'

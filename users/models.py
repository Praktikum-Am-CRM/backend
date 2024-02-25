from django.contrib.auth.models import AbstractUser
from django.db import models


class Manager(AbstractUser):
    profession = models.CharField(max_length=255, verbose_name="Специальность")
    middle_name = models.CharField(max_length=255, verbose_name="Отчество")

    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.middle_name}"

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField(
        verbose_name="correo electrónico",
        unique=True,
    )

    REQUIRED_FIELDS = ["email"]

    class Meta:
        verbose_name = "usuario"
        verbose_name_plural = "usuarios"
        ordering = ["username"]

    def __str__(self) -> str:
        full_name = self.get_full_name().strip()

        if full_name:
            return full_name

        return self.username
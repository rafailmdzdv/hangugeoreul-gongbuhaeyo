"""Module with models to representate users."""
import uuid

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy

from server.apps.users.infrastructure.managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    """User model with required fields."""

    id = models.UUIDField(
        verbose_name=gettext_lazy('Id'),
        primary_key=True,
        default=uuid.uuid4,
    )
    email = models.EmailField(
        verbose_name=gettext_lazy('Email'),
        unique=True,
    )
    date_birth = models.DateField(
        verbose_name=gettext_lazy('Birth Date'),
        auto_now_add=True,
    )
    is_staff = models.BooleanField(
        verbose_name=gettext_lazy('staff status'),
        default=False,
    )

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['date_birth']

    class Meta:
        db_table = 'users'
        verbose_name = gettext_lazy('User')
        verbose_name_plural = gettext_lazy('users')

    def __str__(self) -> str:
        """String representation of user with email."""
        return self.email

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):
    """User manager for `models.User` model."""

    def create_user(
        self,
        email: str,
        password: str,
        **kwargs,
    ) -> AbstractBaseUser:
        """Create default user with required fields."""
        normalized_email = self.normalize_email(email)
        creating_user = self.model(email=normalized_email, **kwargs)
        creating_user.set_password(password)
        creating_user.save()
        return creating_user

    def create_superuser(
        self,
        email: str,
        password: str,
        **kwargs,
    ) -> AbstractBaseUser:
        """Create superuser with required fields."""
        kwargs.setdefault('is_superuser', True)
        kwargs.setdefault('is_staff', True)
        return self.create_user(email=email, password=password, **kwargs)

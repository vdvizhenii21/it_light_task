from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin
from django.db import models


class Role(models.TextChoices):
    CASHIER = 'cashier'
    SELLER = 'seller'
    ACCOUNTANT = 'accountant'


class UserManager(BaseUserManager):

    def create_user(self, email, username, password, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        user = self.model(
                email = self.normalize_email(email),
                username = username,)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, username, password=None):
        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )
        user.set_password(password)  # change password to hash
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractUser):

    email = models.EmailField('email address', blank=False, unique=True)
    username = models.CharField(max_length=25, unique=True)
    bio = models.TextField(blank=True)
    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.SELLER,
    )
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'username'
    objects = UserManager()

    def __str__(self):
        return self.username

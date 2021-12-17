from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)
from django.contrib.auth.hashers import make_password
from .role import Role


class UserManager(BaseUserManager):
    def create_user(self, username, password=None):

        if not username:
            return ValueError("User must have an username")
        user = self.model(username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        user = self.create_user(username=username, password=password)
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField("Username", max_length=15, unique=True)
    password = models.CharField("Password", max_length=256)
    full_name = models.CharField("FullName", max_length=100)
    enabled = models.BooleanField("Enabled", default=True)
    role = models.ForeignKey(Role, related_name="role", on_delete=models.DO_NOTHING)

    def save(self, **kwargs):
        some_salt = "mMUj0DrIK6vgtdIYepkIxN"
        self.password = make_password(self.password, some_salt)
        super().save(**kwargs)

    objects = UserManager()
    USERNAME_FIELD = "username"

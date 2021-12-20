from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)
from django.contrib.auth.hashers import make_password
from django.db.models.aggregates import Max
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
    # username = models.CharField("Username", max_length=15, unique=True)
    id = models.BigAutoField(primary_key=True)
    date_of_birth = models.DateField("Date_Of_Birth")
    document = models.CharField("Document", max_length=50)
    document_type = models.CharField("Document_Type", max_length=50)
    email = models.EmailField("Email", max_length=100, unique=True)
    enabled = models.BooleanField("Enabled", default=True)
    entity = models.CharField("Entity", max_length=100)
    full_name = models.CharField("FullName", max_length=100)
    password = models.CharField("Password", max_length=256)
    phoneNumber = models.CharField("Phone_Number", max_length=25)
    position = models.CharField("Position", max_length=100)

    role = models.ForeignKey(Role, related_name="role", on_delete=models.DO_NOTHING)

    def save(self, **kwargs):
        some_salt = "mMUj0DrIK6vgtdIYepkIxN"
        self.password = make_password(self.password, some_salt)
        super().save(**kwargs)

    objects = UserManager()
    USERNAME_FIELD = "email"

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import UserManager


# defining main user model
class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("email address"), unique=True)
    nickname = models.CharField(_("nickname"), max_length=20, unique=True, default="")
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    # main field for auth
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["nickname"]

    # setting manager for an easy user creation
    objects = UserManager()

    # dander method str
    def __str__(self):
        return self.nickname


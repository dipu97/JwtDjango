from enum import unique

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager
import uuid

# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    _id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(_('First Name') ,max_length=255)
    last_name = models.CharField(_('Last Name'), max_length=255)
    email = models.EmailField(_('Email'), unique=True)
    is_staff = models.BooleanField( default=False)
    is_active = models.BooleanField( default=False)
    date_joined = models.DateTimeField( auto_now_add=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']
    objects = CustomUserManager()
    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')
    def __str__(self):
        return self.email
    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

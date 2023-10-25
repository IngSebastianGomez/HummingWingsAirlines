""" Root user django model definition """

from django.db import models
from django.contrib.auth.models import AbstractBaseUser


class Root(AbstractBaseUser):
    """ Extends native django user model adding new
    features to user definition.

    Python class representation for User database model

    """
    username = models.CharField("Username", max_length=50, unique=True)

    class Meta:
        """ Sets human readable name """
        db_table = "Root"
        verbose_name = "Root"
        verbose_name_plural = "Roots"

    USERNAME_FIELD = 'username'
    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def is_staff(self):
        return True

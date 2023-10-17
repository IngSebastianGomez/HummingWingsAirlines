""" Contains the User model """

from django.db import models
from django.contrib.auth.models import AbstractUser

ROOT = "root"


class Root(AbstractUser):
    """ Extends native django user model adding new
    features to user definition.

    Python class representation for User database model

    """
    first_name = models.CharField(_("Nombre(s)"), 
        max_length=50, null=False, blank=True)
    last_name = models.CharField(_("Apellido(s)"),
        max_length=50, null=False, blank=True)
    rol = models.CharField(_("Rol"), default=ROOT)

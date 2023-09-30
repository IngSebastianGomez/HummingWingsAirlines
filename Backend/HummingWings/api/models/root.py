from django.db import models
from django.contrib.auth.models import AbstractBaseUser

ROOT = "root"

class Root(AbstractBaseUser):
    """ Extends native django user model adding new
    features to user definition.

    Python class representation for User database model

    """
    first_name = models.CharField("Nombre(s)", 
        max_length=50, null=False, blank=True)
    last_name = models.CharField("Apellido(s)",
        max_length=50, null=False, blank=True)
    rol = models.CharField("Rol", default=ROOT)

    USERNAME_FIELD = 'first_name'
    def __str__(self):
        return self.first_name
    
    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(self, app_label):
        return True
    
    def is_staff(self):
        return True
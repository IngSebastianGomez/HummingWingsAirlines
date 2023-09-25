""" Contains the User model """

from django.db import models
from django.contrib.auth.models import AbstractUser

FILE_PATHS = {
    "profile_image": "user/profile_image/user_{}_profile_image_{}.{}",
}

FILE_EXTENSIONS = {
    "profile_image": (".jpeg", ".png", ".jpg")
}

CLIENT = "client"
ADMIN = "admin"

_USER_ROL_CHOICES = (
    (CLIENT = "Cliente"),
    (ADMIN = "Administrador")
)

_STATUS_CHOICES = (
    ("pending", "Pendiente"),
    ("approved", "Aprobado"),
    ("rejected", "Rechazado")
)

_GENDER_CHOICES = (
    ("Masculino", "Masculino"),
    ("Femenino", "Femenino"),
    ("Otro", "Otro")
)

_TYPE_DOCUMENT_CHOICES = (
    ("C.C.", "C.C."),
    ("C.E.", "C.E."),
    ("Pasaporte", "Pasaporte")
)


class User(AbstractUser):
    """ Extends native django user model adding new
    features to user definition.

    Python class representation for User database model

    """
    first_name = models.CharField(_("Nombre(s)"), 
        max_length=50, null=False, blank=True)
    last_name = models.CharField(_("Apellido(s)"),
        max_length=50, null=False, blank=True)
    birth_date = models.DateField(_("Fecha de Nacimiento"), 
        null=True, blank=True)
    email = models.EmailField("Correo", unique=True)
    rol = models.CharField(_("Rol"), choices=_USER_ROL_CHOICES, default=CLIENT)
    type_document = models.CharField("Tipo de documento", max_length=255,
        choices=_TYPE_DOCUMENT_CHOICES, default="C.C.")
    document = models.CharField("Identificación", max_length=255, unique=True)
    address = models.CharField("Dirección", max_length=255)
    gender = models.CharField("Género", max_length=255, 
        choices=_GENDER_CHOICES, default="Otro")
    status = models.CharField("Estado", max_length=255, choices=_STATUS_CHOICES,
        default="pending")
    profile_image = models.FileField(_("Imagen de perfil"), 
        upload_to="user/profile_image", null=True, blank=True)
   
    
    class Meta:
        """ Sets human readable name """
        db_table = "Usuarios"
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"
        
    def __str__(self):
        return f"{self.id}. {self.get_full_name}. {self.rol}"

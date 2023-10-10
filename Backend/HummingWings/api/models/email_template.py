""" Contains the Email Template model """

from django.db import models

CLIENT_REGISTER_CONFIRMATION = "client_register_confirmation"

_TEMPLATES = (
    (
        CLIENT_REGISTER_CONFIRMATION,
        "Confirmación de registro - Cliente"
    ),
)


class EmailTemplate(models.Model):
    """
    Python class representation for EmailTemplate database model

    """

    email_id = models.CharField(
        "ID del correo", choices=_TEMPLATES, max_length=128)
    subject = models.CharField("Asunto", max_length=255)
    template = models.TextField("Plantilla")

    class Meta:
        """ Sets human readable name """
        # pylint: disable=too-few-public-methods
        constraints = [
            models.UniqueConstraint(
                fields=['email_id'], name='email_id_uniqueness')]

        indexes = [models.Index(fields=['email_id'], name='email_id_idx')]

        db_table = "email_template"
        verbose_name = "Plantilla de correo"
        verbose_name_plural = "Plantillas de correos"

    def __str__(self):
        return f"{self.email_id}"

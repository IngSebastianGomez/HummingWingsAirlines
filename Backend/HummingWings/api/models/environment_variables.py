""" Contains the Environment Variables model """

from django.db import models


class EnvironmentVariables(models.Model):
    """ Contains each Environment Variable with its characteristics."""
    TYPE_CHOICES = (
        ("string", "Cadena"),
        ("float", "Decimal"),
        ("integer", "Entero"),
        ("boolean", "Booleano"))

    var_name = models.CharField("Nombre de variable", max_length=255)
    var_value = models.CharField("Valor", max_length=700)
    var_type = models.CharField(
        "Tipo de variable", max_length=15, choices=TYPE_CHOICES)
    description = models.CharField("Descripción", max_length=255)

    class Meta:  # pylint: disable=too-few-public-methods
        """ Sets human readable name """
        constraints = [
            models.UniqueConstraint(
                fields=['var_name'],
                name='envs_uniqueness'
            )
        ]

        indexes = [
            models.Index(fields=['var_name'], name='envs_var_name_idx')
        ]

        verbose_name = "Variable de entorno"
        verbose_name_plural = "Variables de entorno"

    def __str__(self):
        return f'[{self.var_type}] {self.var_name}: {self.var_value}'

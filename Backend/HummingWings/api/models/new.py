""" Contains the New model """
from django.db import models
from django_extensions.db.models import TimeStampedModel

class New(TimeStampedModel):
    """ New model definition. """
    title = models.CharField("Titulo", max_length=200)
    content = models.TextField("Contenido", max_length=250)
    new_image = models.FileField("Imagen de noticia",
        upload_to="news/new_image", null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        """ Sets human readable name """
        db_table = "New"
        verbose_name = "New"
        verbose_name_plural = "News"

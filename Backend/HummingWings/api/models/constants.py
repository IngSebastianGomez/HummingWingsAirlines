""" Constants definition """

CLIENT = "cliente"
ADMIN = "administrador"
ROOT = "root"

_USER_ROL_CHOICES = (
    (CLIENT, "Cliente"),
    (ADMIN, "Administrador")
)

PENDING = "pending"
APPROVED = "approved"
REJECTED = "rejected"

_STATUS_CHOICES = (
    (PENDING, "Pendiente"),
    (APPROVED, "Aprobado"),
    (REJECTED, "Rechazado")
)

MALE = "masculino"
FEMALE = "femenino"
OTHER = "otro"

_GENDER_CHOICES = (
    (MALE, "Masculino"),
    (FEMALE, "Femenino"),
    (OTHER, "Otro")
)

CC = "C.C."
CE = "C.E."
PASSPORT = "Pasaporte"

_DOCUMENT_TYPE_CHOICES = (
    (CC, "C.C."),
    (CE, "C.E."),
    (PASSPORT, "Pasaporte")
)

############### ERROR CODE MESSAGE ####################
_STATUS_400_MESSAGE = "Cuerpo con estructura inválida"
_STATUS_401_MESSAGE = "No tienes permiso para ejecutar esta acción"
_STATUS_403_MESSAGE = "No tienes permiso para ejecutar esta acción"
_STATUS_404_MESSAGE = "No se encontró el recurso solicitado"
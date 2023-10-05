""" Constants definition """

CLIENT = "Cliente"
ADMIN = "Administrador"
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

_TYPE_DOCUMENT_CHOICES = (
    ("C.C.", "C.C."),
    ("C.E.", "C.E."),
    ("Pasaporte", "Pasaporte")
)
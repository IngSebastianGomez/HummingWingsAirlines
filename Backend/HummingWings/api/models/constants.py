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
CHECKIN = "checkin"

_STATUS_CHOICES = (
    (PENDING, "Pendiente"),
    (APPROVED, "Aprobado"),
    (REJECTED, "Rechazado")
)
_STATUS_CHOICES_TICKET = (
    (PENDING, "Pendiente"),
    (APPROVED, "Aprobado"),
    (REJECTED, "Rechazado"),
    (CHECKIN, "Check-in")
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
TI = "Tarjeta de identidad"

_DOCUMENT_TYPE_CHOICES = (
    (CC, "C.C."),
    (CE, "C.E."),
    (PASSPORT, "Pasaporte"),
    (TI, "T.I.")
)

ROUND_TRIP = "round_trip"
ONE_WAY = "one_way"

############### ERROR CODE MESSAGE ####################
_STATUS_400_MESSAGE = "Cuerpo con estructura inválida"
_STATUS_401_MESSAGE = "No tienes permiso para ejecutar esta acción"
_STATUS_403_MESSAGE = "No tienes permiso para ejecutar esta acción"
_STATUS_404_MESSAGE = "No se encontró el recurso solicitado"

################## REGEX ##############################
EMAIL_REGEX = r"(?!.*\.\.)(?!.*@.*\.\.)(?!.*\.$)[a-zA-Z0-9._-]*[a-zA-Z0-9]+(\.[a-zA-Z0-9]+)*@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}"
PASSWORD_REGEX = r"^.*(?=.{8,100})(?=.*[a-zA-Z])(?=.*[a-z])(?=.*\d)[a-zA-Z0-9].*$"
DATE_REGEX = r"(19[2-9]\d|20[0-1]\d|202[0-3])-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])"

################# TYPE FLIGHTS #################
DIRECT = "directo"
_TYPE_FLIGHT_CHOICES = (
    (DIRECT, "Directo"),
)

FIRST_CLASS = ['1', '2']
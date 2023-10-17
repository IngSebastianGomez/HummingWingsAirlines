===================================
 Recurso de administración de Root
===================================

Recurso POST
------------

.. http:post:: /api/v1/entrenchment_property_change

Crea un nuevo usuario Root

**Campos obligatorios**

.. list-table::
   :widths: 20 20 30 30
   :header-rows: 1

   * - Campo
     - Tipo
     - Condiciones
     - Descripción

   * - username
     - Cadena
     - (Hay que considerarlo, qué expresión regular configuramos? Decisión de diseño)
     - Nombre de usuario con el que ingresará a la plataforma

   * - password
     - Cadena
     - Cumple con la expresión regular: '^.*(?=.{8,100})(?=.*[a-zA-Z])(?=.*[a-z])(?=.*\d)[a-zA-Z0-9].*$'
     - Contraseña con la que ingresará a la plataforma. Es encriptada antes de almacenarse

**Ejemplo de petición**

.. sourcecode:: http

    POST /api/v1/entrenchment_property_change HTTP/1.1
    ## Este verbo necesita el header siguiente para manejar la autenticación
    Authorization: Bearer eyaslm234jkh6ñl34k2354jkh...
    Content-Type: application/json

    {
        "username": "root",
        "password": "contraseña_segura_para_root"
    }

**Ejemplos de respuesta**

.. sourcecode:: http

## Acá viene la versión de HTTP que estamos usando. Eso hay que consultarlo con front
    HTTP/1.1 201 CREATED
    Content-Type: application/json

    {
        "inserted": 1
    }

.. sourcecode:: http

    HTTP/1.1 400 BAD_REQUEST
    Content-Type: application/json

    {
        "code": "invalid_body",
        "detail": "Cuerpo con estructura inválida",
        "data": {
            "password": [
                "Este campo es requerido."
             ]
        }
    }

.. sourcecode:: http

    HTTP/1.1 401 UNAUTHORIZED
    Content-Type: application/json

    {
         "code": "unauthorized",
         "detailed": "Sesión expirada o no autorizado"
    }

.. sourcecode:: http

    HTTP/1.1 401 UNAUTHORIZED
    Content-Type: application/json

    {
        "code": "do_not_have_permission",
        "detailed": "No tienes permiso para ejecutar esta acción"
    }

.. sourcecode:: http

    HTTP/1.1 409 CONFLICT
    Content-Type: application/json

    {
        "code": "integrity_error",
        "detailed": "Ya existe un usuario registrado con ese nombre de usuario"
    }

:status 201: Usuario creado exitosamente.
:status 400: Cuerpo con estructura inválida.
:status 401: Sesión expirada o no autorizado.
:status 409: Ya existe un usuario registrado con ese nombre de usuario.

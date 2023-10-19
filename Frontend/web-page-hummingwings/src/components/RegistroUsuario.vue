<template>
  <div class="container-sm mt-5">
    <form>
      <div class="mb-3">
        <label for="exampleInputName1" class="form-label">Nombre</label>
        <input type="email" class="form-control" id="exampleInputName1">
      </div>

      <div class="mb-3">
        <label for="exampleInputLastName1" class="form-label">Apellido</label>
        <input type="email" class="form-control" id="exampleInputLastName1">
      </div>

      <div class="mb-3">
        <label for="identityDocument" class="form-label">Documento de identidad</label>
        <select id="identityDocument" class="form-select" aria-label="Default select example">
          <option selected>Documento de identidad</option>
          <option value="1">Cédula de Ciudadanía</option>
          <option value="2">Pasaporte</option>
        </select>
      </div>

      <div class="mb-3">
        <label for="exampleInputNumeroIdentificacion1" class="form-label">Número de identificación</label>
        <input type="email" class="form-control" id="exampleInputNumeroIdentificacion1">
      </div>

      <div class="mb-3">
        <label for="birthday" class="form-label">Fecha de Nacimiento</label>
        <input type="date" id="birthday" class="form-control" min="1924/01/01" data-date-end-date="15/10/2022">
      </div>

      <div class="mb-3">
        <label for="gender" class="form-label">Genero</label>
        <select id="gender" class="form-select" aria-label="Default select example">
          <option selected>Genero</option>
          <option value="1">Hombre</option>
          <option value="2">Mujer</option>
          <option value="3">Prefiero no decirlo</option>
        </select>
      </div>

      <div class="mb-3">
        <label for="InputPhoneNumber" class="form-label">Numero de telefono</label>
        <input type="phoneNumber" class="form-control" id="InputPhoneNumber">
      </div>

      <div class="mb-3">
        <label for="exampleInputEmail1" class="form-label">Correo Electronico</label>
        <input type="email" class="form-control" id="exampleInputEmail1">
      </div>

      <div class="mb-3">
        <label for="exampleInputPassword1" class="form-label">Contraseña</label>
        <input type="password" class="form-control" id="exampleInputPassword1">
      </div>

      <div class="mb-3">
        <label for="contactName" class="form-label">Nombre de un contacto</label>
        <input type="email" class="form-control" id="contactName">
      </div>
      
      <div class="mb-3">
        <label for="numberContactName" class="form-label">Numero de un contacto</label>
        <input type="password" class="form-control" id="numberContactName">
      </div>

      <div class="d-grid gap-2 pb-5">
        <button class="btn btn-primary" type="button">Subir foto de perfil</button>
        <button class="btn btn-dark" type="button" style="background-color: #182a3f; border-radius: 40px;">Enviar</button>
      </div>
      
    </form>
  </div>
</template>

<style>
  .container-sm{
    background: linear-gradient(112deg, #009D71 20.89%, rgba(0, 157, 117, 0.00) 89.16%);
    border-radius: 40px;
    padding: 1rem;
  }
  body{
    background-color: #171A4A;
  }
</style>
<template>
  <div class="container-sm mt-5 degradade-root" style="background: linear-gradient(114deg, #881610 0%, #019970 100%);">
    <h1>Crear usuario administrador</h1>
    <div class="container" style="padding-left: 4rem; padding-right: 4rem; padding-top: 2rem;">
      <form>
        <div class="mb-3">
          <label for="EmailAdmin" class="form-label">Correo electronico</label>
          <input type="email" class="form-control" id="EmailAdmin">
        </div>
        <div class="mb-3">
          <label for="Password" class="form-label">Contraseña</label>
          <input type="password" class="form-control" id="Password">
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
        <div class="d-grid gap-2 pb-5">
          <button class="btn btn-dark" type="button" style="background-color: #182a3f; border-radius: 40px;">Crear</button>
        </div>
      </form>
    </div>
  </div>
</template>

<style>

</style>
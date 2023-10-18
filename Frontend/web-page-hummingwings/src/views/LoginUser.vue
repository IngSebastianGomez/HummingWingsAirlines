<template>
  <div class="container-sm mt-5" style="max-width: 600px;">
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
          <router-link to="registro" style="color: white;">¿Aun no estas registrado?</router-link>
        </div>
        <div class="d-grid gap-2 pb-5">
          <button class="btn btn-dark" type="button" style="background-color: #182a3f; border-radius: 40px;">Ingresar</button>
        </div>
      </form>
    </div>
  </div>
</template>

<style>
  .container-sm{
    background: linear-gradient(114deg, #009D71 0%, rgba(0, 157, 117, 0.00) 100%);
    padding: 1rem;
    border-radius: 40px;
    margin-bottom: 2rem;
  }
</style>
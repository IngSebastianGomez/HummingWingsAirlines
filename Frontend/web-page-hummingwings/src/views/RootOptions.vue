<script>
</script>

<template>
  <div class="container">
    <div class="row bg-transparent" style="padding: 1.5rem;">
      <div class="col bg-transparent">
        <p class="fs-1 text-danger justify-center">Control de Root</p>
      </div>
    </div>
    <div class="row bg-transparent justify-content-evenly" style="padding-bottom: 1rem;">
      <div class="col-4">
          <router-link to="/managePromotions" class="btn btn-danger btn-lg btn-block">Agregar Administrador</router-link>
      </div>
      <div class="col-4">
          <router-link to="/manageFlights" class="btn btn-danger btn-lg btn-block">Editar Administrador</router-link> 
      </div>
    </div>
  </div>
</template>

<style>
@import url('https://fonts.googleapis.com/css2?family=Aclonica&display=swap');

.text-danger{
    font-family: 'Aclonica', sans-serif;
  }
  
</style>

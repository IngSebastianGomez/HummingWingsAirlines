<script>
</script>

<template>
  <div class="container">
    <div class="row bg-transparent" style="padding: 1.5rem;">
      <div class="col bg-transparent">
        <h1 class="myText">Bienvenido Admin</h1>
        <br>
        <p class="myText">¿Que desea hacer?</p>
      </div>
    </div>
    <div class="row bg-transparent justify-content-evenly" style="padding-bottom: 1rem;">
      <div class="col-4">
          <router-link to="/" class="btn btn-primary btn-lg btn-block">Administrar Promociones</router-link>
      </div>
      <div class="col-4">
          <router-link to="/manageFlights" class="btn btn-primary btn-lg btn-block">Administrar Vuelos</router-link> 
      </div>
    </div>
  </div>
</template>

<style>
@import url('https://fonts.googleapis.com/css2?family=Aclonica&display=swap');

.myText{
    font-family: 'Aclonica', sans-serif;
    color: white;
  }
  
</style>
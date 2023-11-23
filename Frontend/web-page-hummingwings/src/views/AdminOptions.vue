<template>
  <div class="container">
    <div class="row bg-transparent" style="padding: 1.5rem;">
      <div class="col bg-transparent">
        <h1 class="myText" style="color: white;">Bienvenido Admin</h1>
        <br>
        <p class="myText" style="color: white;">¿Que desea hacer?</p>
      </div>
    </div>
    <div class="row bg-transparent justify-content-evenly" style="padding-bottom: 1rem;">
      <div class="col-4">
          <router-link to="/" class="btn btn-primary btn-lg btn-block">Administrar Promociones</router-link>
      </div>
      <div class="col-4">
          <router-link to="/manageFlight" class="btn btn-primary btn-lg btn-block">Administrar Vuelos</router-link> 
      </div>
    </div>
  </div>
</template>

<style>
  
</style>
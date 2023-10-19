<template>
    <div style="color: white;">
      <h1>Perfil de usuario</h1>
      <p>id: {{ id }} </p>
      <p>Nombre de usuario: {{ username }}</p>
      <p>tipo: {{ type }}</p>
      <p>token: {{ token }}</p>
      <div>sesion: {{ loggedIn }}</div>

      <div class="row bg-transparent" style="padding: 1.5rem;">
      <div class="col bg-transparent">
        <p class="fs-1 text-danger" style="font-family: ;">Opciones de control del Root</p>
      </div>
    </div>

    <div class="row bg-transparent justify-content-evenly" style="padding-bottom: 1rem;">
      <div class="col-4">
          <router-link to="/CreateAdmin" class="btn btn-danger btn-lg btn-block">Agregar Admin</router-link> 
      </div>
      <div class="col-4">
          <router-link to="/ListaAdministradores" class="btn btn-danger btn-lg btn-block">Editar Admin</router-link> 
      </div>
    </div>   
    </div>
    
  </template>
  
  <script>
  import { mapState } from 'vuex'; // Si estás utilizando Vuex
  
  export default {
  computed: {
    ...mapState(['username', 'id', 'type', 'loggedIn', 'token']),
    // Recupera el token desde el Local Storage en las propiedades computadas
    
  },
};
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Aclonica&display=swap');

.text-danger{
        font-family: 'Aclonica', sans-serif;
}

.center {
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
}
  
</style>
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
        <p class="fs-1 myText" style="color: red;">Opciones de control del Root</p>
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
    <button @click="handleLogout">Cerrar Sesión</button>
    </div>
    
  </template>
  
  <script>
  import { mapState, mapActions } from 'vuex'; // Si estás utilizando Vuex
  
  export default {
  computed: {
    ...mapState(['username', 'id', 'type', 'loggedIn']),
    // Recupera el token desde el Local Storage en las propiedades computadas
    token() {
      return localStorage.getItem('sessionToken') || ''; // Si no hay token en el Local Storage, devuelve una cadena vacía
    },
  },
  methods: {
  ...mapActions(['logout']), // Importa la acción de cierre de sesión
  handleLogout() {
    this.logout(); // Llama a la acción de cierre de sesión
    this.$router.push('/'); // Redirige al usuario a la página de inicio de sesión o a la ruta deseada
  },
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
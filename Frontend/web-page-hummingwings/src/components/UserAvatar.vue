<template>
    <div>
      <button
        class="btn btn-link"
        id="avatar-button"
        data-bs-toggle="dropdown"
        aria-expanded="false"
      >
        <img
          src="https://cdn4.iconfinder.com/data/icons/avatars-xmas-giveaway/128/batman_hero_avatar_comics-512.png" 
          alt="Avatar"
          class="avatar"
        />
      </button>
  

      <div class="dropdown-menu" aria-labelledby="avatar-button">
        <!-- Opciones del menú desplegable -->
        <a class="dropdown-item" href="#">Perfil</a>
        <a class="dropdown-item" href="#">Configuración</a>
        <div class="dropdown-divider"></div>
        <a class="dropdown-item" href="#" @click="handleLogout">Cerrar Sesión</a>
      </div>
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
  
<style scoped>
  .avatar {
    width: 40px; /* Establece el tamaño de tu avatar */
    height: 40px;
    border-radius: 50%; /* Crea una forma circular */
    object-fit: cover; /* Ajusta la imagen al tamaño del avatar */
  }
</style>
  
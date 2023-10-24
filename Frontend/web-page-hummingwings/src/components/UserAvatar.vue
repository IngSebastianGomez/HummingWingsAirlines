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
      <a class="dropdown-item" @click="irVisualDatos">Perfil</a> <!-- Agrega un enlace a la vista de perfil -->
      <a class="dropdown-item" href="#">Configuración</a>
      <div class="dropdown-divider"></div>

      <!-- Agrega una opción adicional si el rol es 'administrador' -->
      <a v-if="rol === 'administrador'" class="dropdown-item" @click="irARutaAdmin">Admin</a>

      <a class="dropdown-item" href="#" @click="handleLogout">Cerrar Sesión</a>
    </div>
  </div>
</template> 

<script>
import { mapState, mapActions } from 'vuex';

export default {
  computed: {
    ...mapState(['username', 'id', 'type', 'loggedIn', 'rol']), // Asegúrate de incluir 'rol' en las propiedades computadas
    token() {
      return localStorage.getItem('sessionToken') || '';
    },
  },
  methods: {
    ...mapActions(['logout']),
    handleLogout() {
      this.logout();
      this.$router.push('/');
    },
    irARutaAdmin() {
      // Agrega aquí la lógica para redirigir a la ruta de opciones de administrador
      this.$router.push('/AdminOptions');
    },
    irVisualDatos() {
      // Agrega aquí la lógica para redirigir a la ruta de opciones de administrador
      this.$router.push('/VisualDatos');
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
  .dropdown-item {
  cursor: pointer; /* Establece el cursor como puntero */
}

</style>
  
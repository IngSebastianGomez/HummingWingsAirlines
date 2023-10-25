<template>
  <div class="row align-items-center" style="padding-right: 1rem;">
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

    <div class="dropdown-menu custom-dropdown-menu" aria-labelledby="avatar-button">
      <!-- Opciones del menú desplegable -->
      <a class="dropdown-item" @click="irVisualDatos">Perfil</a>
      <a class="dropdown-item" href="#">Configuración</a>
      <div class="dropdown-divider"></div>
      <a v-if="rol === 'administrador'" class="dropdown-item" @click="irARutaAdmin">Admin</a>
      <a class="dropdown-item" href="#" @click="handleLogout">Cerrar Sesión</a>
    </div>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex';
import axios from 'axios';

export default {
  computed: {
    ...mapState(['username', 'id', 'type', 'loggedIn', 'rol','token']),
    tokenn() {
      return localStorage.getItem('sessionToken') || '';
    },
  },
  methods: {
    ...mapActions(['logout']),
    handleLogout() {
      // Realiza la solicitud PATCH al cerrar sesión
      axios.patch('http://127.0.0.1:8000/api/v1/auth/', null, {
        headers: {
          'Authorization': `Bearer ${this.token}`,
        },
      })
        .then(() => {
          // Maneja la respuesta exitosa (si es necesario)
          console.log('La sesión se ha deshabilitado con éxito.');
        })
        .catch(error => {
          // Maneja los errores (si es necesario)
          if (error.response.status === 400) {
            console.log('Solicitud incorrecta: verifica la estructura de la solicitud JSON y el encabezado de autorización.');
          } else if (error.response.status === 404) {
            console.log('La sesión no se encontró. Verifica el token de autorización.');
          } else {
            console.log(`Error inesperado: ${error.response.status}`);
          }
        });

      // Luego, realiza el logout localmente y redirige al usuario
      this.logout();
      this.$router.push('/');
    },
    irARutaAdmin() {
      // Agrega aquí la lógica para redirigir a la ruta de opciones de administrador
      this.$router.push('/AdminOptions');
    },
    irVisualDatos() {
      // Agrega aquí la lógica para redirigir a la ruta de perfil o visualización de datos
      this.$router.push('/VisualDatos');
    },
  },
};
</script>

<style scoped>
  .avatar {
    width: 40px;
    height: 40px;
    border-radius: 50%;
    object-fit: cover;
  }
  .custom-dropdown-menu {
    width: 200px; /* Establece el ancho deseado para el menú desplegable */
  }
  .dropdown-item {
    cursor: pointer;
  }
</style>

<template>
  <div class="MyHeader">
    <div class="d-flex">
      <a href="#">
        <img src="../assets/Logo_HummingWings.png" class="mr-3">
      </a>
      <h1 class="myText" id="titulo">Humming <br> Wings</h1>
    </div>
    
    <div class="btn-group">
    <!-- Muestra el botón de inicio de sesión si el usuario no ha iniciado sesión -->
    <button-session v-if="!loggedIn"></button-session>
    
    <!-- Muestra el avatar si el usuario ha iniciado sesión -->
    <user-avatar v-else></user-avatar>
  </div>
  </div>
</template>


<script>
import { mapState } from 'vuex';
import ButtonSession from './ButtonSession.vue';
import UserAvatar from './UserAvatar.vue';
export default {
  name: 'MyHeader',
  components: {
    'button-session': ButtonSession,
    'UserAvatar': UserAvatar,
  },
  computed: {
    ...mapState(['loggedIn']),
  },
  data() {
    return {
      message: 'Hello from MyHeader.vue!'
    }
  }
}
</script>


<style scoped>
/* Estilos CSS para tu componente Vue.js */
.MyHeader {
  position: relative; /* Permite posicionar elementos hijos con respecto a este elemento */
  display: flex; /* Utiliza flexbox para controlar la alineación y el espaciado */
  justify-content: space-between; /* Alinea los elementos a los extremos */
  align-items: center; /* Alinea elementos verticalmente al centro */
  padding: 5px 14px; /* Agrega espaciado interior para separar el contenido del borde */
  background-color: green; /* Establece el color de fondo del encabezado */
}

.MyHeader img {
  max-height: 50px; /* Ajusta la altura máxima del logotipo según tus necesidades */
  max-width: 100%; /* Asegura que el logotipo no se extienda más allá del contenedor */
  margin-right: 10px; /* Opcional: agrega un margen derecho para separar el logotipo de otros elementos */
  margin: auto; /* Centra la imagen horizontalmente */
}

/* Cambiar la fuente del elemento con ID "titulo" */
.titulo {
  font-family: "Nueva Fuente", sans-serif;
  color: white;
  font-size: 24px; /* Add this line to adjust the font size */
}

/* Reemplaza "Nueva Fuente" con el nombre de la fuente que desees utilizar */

.nav{
  font-family: "Nueva Fuente", sans-serif;
  font-size: 20px;
  padding: 10px;
  margin: 10px;
  margin-left: auto; /* Alinea el elemento a la derecha */
}

.nav a {
  margin-right: 10px; /* Agrega un margen a la derecha de cada enlace */
}
</style>

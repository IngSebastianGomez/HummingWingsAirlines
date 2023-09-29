<template>
  <div class="MyHeader">
    <div class="d-flex">
      <img src="../assets/Logo_HummingWings.png" class="mr-3">
      <h1 id="titulo">Humming <br> Wings</h1>
    </div>
    <nav class="nav ml-auto"> <!-- Aplica la clase ml-auto aquí -->
      <a href="#">Inicio</a>
      <a href="#">Servicios</a>
      <a href="#">Nosotros</a>
      <a href="#">Contacto</a>
    </nav>
    <b-dropdown id="dropdown-dropleft" dropleft text="Sesión" variant="primary" class="m-2">
      <b-dropdown-item>Iniciar Sesión</b-dropdown-item>
      <b-dropdown-item>Registrarse</b-dropdown-item>
      <b-dropdown-item>Opción 3</b-dropdown-item>
    </b-dropdown>
  </div>
</template>


<script>
export default {
  name: 'MyHeader',
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
  color: white;
  font-family: "Nueva Fuente", sans-serif;
  font-size: 20px;
  padding: 10px;
  margin: 10px;
  text-align: right;
}
.nav a {
  margin-right: 15px;
}

</style>

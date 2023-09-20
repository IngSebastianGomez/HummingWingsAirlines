<template>
    <div class="my-component">
        <img src="../assets/Logo_HummingWings.png">
        <h1 id="titulo">Humming <br> Wings</h1>
        <a href="#" class="btn btn-primary">Foro</a>
        <a href="#" class="btn btn-primary">Iniciar Sesión</a>
    </div>
</template>

<script>
export default {
    name: 'MyComponent',
    data() {
        return {
            message: 'Hello from MyComponent'
        }
    }
}
</script>

<style scoped>
/* Estilos CSS para tu componente Vue.js */
.my-component {
  position: relative; /* Permite posicionar elementos hijos con respecto a este elemento */
  display: flex; /* Utiliza flexbox para controlar la alineación y el espaciado */
  justify-content: flex-start; /* Alinea elementos a la izquierda */
  align-items: center; /* Alinea elementos verticalmente al centro */
  padding: 16px 14px; /* Agrega espaciado interior para separar el contenido del borde */
  background-color: green; /* Establece el color de fondo del encabezado */

}

.my-component img {
  max-height: 50px; /* Ajusta la altura máxima del logotipo según tus necesidades */
  max-width: 100%; /* Asegura que el logotipo no se extienda más allá del contenedor */
  margin-right: 10px; /* Opcional: agrega un margen derecho para separar el logotipo de otros elementos */
}

/* Cambiar la fuente del elemento con ID "titulo" */
.titulo {
  font-family: "Nueva Fuente", sans-serif;
  color: white;
  /* Reemplaza "Nueva Fuente" con el nombre de la fuente que desees utilizar */
}

</style>

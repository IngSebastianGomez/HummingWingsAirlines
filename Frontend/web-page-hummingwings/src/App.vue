<template>
  <div id="app">
    <header>
      <MyHeader/>
    </header>
  </div>
</template>


<script>
import MyHeader from './components/Header.vue'

export default {
  name: 'App',
  components: {
    MyHeader
  }

}

// Función para mostrar la vista oculta
function mostrarVistaOculta() {
  //var vistaOculta = document.getElementById("vista-oculta");
  //vistaOculta.style.display = "block";
  window.location.href = "https://www.example.com"; // Replace with the URL of the page you want to open
}

// Función para manejar el evento de teclado
function handleKeyPress(event) {
  if (event.ctrlKey && event.shiftKey && event.key.toLowerCase() === "r") {
    mostrarVistaOculta();
  }
}
// Agregar un escuchador de eventos para detectar la combinación de teclas
document.addEventListener("keydown", handleKeyPress);
</script>

<style>
#app {
  background-color: #182a3f;
  min-height: 100vh;
}

body{
  margin: 0; 
  padding: 0;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  background-color: #182a3f;
  min-height: 100vh;
}

</style>

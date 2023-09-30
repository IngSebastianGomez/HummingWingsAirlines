<template>
  <div id="app">
    <header>
      <MyHeader/>
    </header>
    <!--<body><RouterView> </RouterView></body>-->
    <div>
      <CarouselSlider v-if="isHomePage" />
      <h1>{{ $route.path }}</h1>
    </div>
    <div>
      <RouterView> </RouterView>
    </div>
  </div>
</template>


<script>
import { useRoute } from 'vue-router'
import MyHeader from './components/Header.vue'
import CarouselSlider from './components/CarouselSliderAd.vue'


export default {
  name: 'App',
  components: {
    MyHeader,
    CarouselSlider,
  },
  setup() {
    const route = useRoute()
    const isHomePage = route.path === '/' 

    console.log('isHomePage:', isHomePage)
    console.log('Current Route:', route.path)
    
    return {
      isHomePage,
    }
  },
}

// Función para mostrar la vista oculta
function mostrarVistaOculta() {
  window.location.href = "http://localhost:8080/#/login"; // Replace with the URL of the page you want to open
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

</style>

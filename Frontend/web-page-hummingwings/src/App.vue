<template>
  <div id="app">
    <header>
      <MyHeader/>
    </header>
    <div>
      <RouterView> </RouterView>
    </div>
  </div>
</template>


<script>
import { useRoute, useRouter } from 'vue-router'
import MyHeader from './components/Header.vue'

export default {
  name: 'App',
  components: {
    MyHeader,
  },
  setup() {
    const route = useRoute()
    const router = useRouter() // Accede a $router desde el contexto setup

    const isHomePage = route.path === '/' 

    console.log('isHomePage:', isHomePage)
    console.log('Current Route:', route.path)
    
    // Función para mostrar la vista oculta
    const mostrarVistaOculta = () => {
      // Usamos router para ir a la vista oculta de root LoginRoot
      router.push('/LoginRoot');
    }

    // Función para manejar el evento de teclado
    function handleKeyPress(event) {
      if (event.ctrlKey && event.shiftKey && event.key.toLowerCase() === "r") {
        mostrarVistaOculta();
      }
    }
    
    // Agregar un escuchador de eventos para detectar la combinación de teclas
    document.addEventListener("keydown", handleKeyPress);

    return {
      isHomePage,
    }
  },
}
</script>


<style>
@import url('https://fonts.googleapis.com/css2?family=Aclonica&display=swap');

.myText{
    font-family: 'Aclonica', sans-serif;
  }
#app {
  background-color: #182a3f;
  min-height: 100vh;
}

</style>

<!-- Header.vue esto esta re paila -->
<template>
    <header>
      <logo></logo>
      <div class="header-content">
        <h1>{{ pageTitle }}</h1>
        <login-button></login-button>
      </div>
    </header>
  </template>
  
  <script>
  import Logo from "./Logo.vue";
  import LoginButton from "./LoginButton.vue";
  
  export default {
    components: {
      Logo,
      LoginButton,
    },
    data() {
      return {
        pageTitle: "Página Principal",
      };
    },
  };
  </script>
  
  <style scoped>
  /* Estilos CSS para tu encabezado (header) */
  </style>
  
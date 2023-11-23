<template>
    <div class="container-sm mt5">
      <div class="row" style="display: flex;">
        <h1>Mi Perfil</h1>
      </div>
      <div class="row" v-if="loggedIn">
        <h1>Informacion de la cuenta</h1>
        <p><strong>Nombre de Usuario:</strong> {{ username }}</p>
        <p><strong>ID:</strong> {{ id }}</p>
        <p><strong>Tipo:</strong> {{ type }}</p>
        <p><strong>Email:</strong> {{ email }}</p>
        <h1>Informacion del usuario</h1>
        <p><strong>Nombre:</strong> {{ first_name }} {{ last_name }}</p>
        <p><strong>Celular:</strong> {{ cellphone }}</p>
        <p><strong>Tipo de Documento:</strong> {{ document_type }}</p>
        <p><strong>Documento:</strong> {{ document }}</p>
        <p><strong>Rol:</strong> {{ rol }}</p>
        <p><strong>Género:</strong> {{ gender }}</p>
        <h1>Info adicional</h1>
        <p><strong>Estado:</strong> {{ status }}</p>
        <p><strong>Token:</strong> {{ token }}</p>
        <p><strong>Refresh:</strong> {{ refresh }}</p>
        <button class="btn btn-primary" @click="logout">Cerrar Sesión</button>
      </div>
      <div v-else>
        <p>Debes iniciar sesión para ver tu perfil.</p>
      </div>
    </div>
  </template>
  
  <script>
  import { mapState, mapActions } from 'vuex';
  
  export default {
    computed: {
      ...mapState(['id', 'username', 'type', 'loggedIn', 'token', 'refresh', 'email', 'cellphone', 'first_name', 'last_name', 'gender', 'rol', 'status', 'document', 'document_type']),
    },
    methods: {
      ...mapActions(['logout']),
    },
  };
  </script>

<style scoped>
  .profile-container {
    text-align: center;
    max-width: 600px;
    margin: 0 auto;
    padding: 20px;
  }

  .h1 {
    font-size: 24px;
    color: white;
  }

  .p {
    font-size: 18px;
    color: #000000;
    margin: 5px 0;
  }

  button {
    background-color: #3498db;
    color: white;
    border: none;
    padding: 10px 20px;
    margin-top: 20px;
    font-size: 16px;
    cursor: pointer;
  }

  button:hover {
    background-color: #258cd1;
  }
</style>

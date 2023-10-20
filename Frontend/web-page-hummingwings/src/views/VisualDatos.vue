<template>
    <div>
      <h1>Mi Perfil</h1>
      <div v-if="loggedIn">
        <p><strong>ID:</strong> {{ id }}</p>
        <p><strong>Nombre de Usuario:</strong> {{ username }}</p>
        <p><strong>Tipo:</strong> {{ type }}</p>
        <p><strong>Email:</strong> {{ email }}</p>
        <p><strong>Celular:</strong> {{ cellphone }}</p>
        <p><strong>Nombre:</strong> {{ first_name }} {{ last_name }}</p>
        <p><strong>Género:</strong> {{ gender }}</p>
        <p><strong>Rol:</strong> {{ rol }}</p>
        <p><strong>Estado:</strong> {{ status }}</p>
        <p><strong>Documento:</strong> {{ document }}</p>
        <p><strong>Tipo de Documento:</strong> {{ document_type }}</p>
        <p><strong>Token:</strong> {{ token }}</p>
        <p><strong>Refresh:</strong> {{ refresh }}</p>
        <button @click="logout">Cerrar Sesión</button>
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

<style>
  .profile-container {
    text-align: center;
    max-width: 600px;
    margin: 0 auto;
    padding: 20px;
  }

  h1 {
    font-size: 24px;
    color: #333;
  }

  p {
    font-size: 18px;
    color: #555;
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

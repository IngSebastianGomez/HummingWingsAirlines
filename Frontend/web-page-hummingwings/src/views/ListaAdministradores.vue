<template>
    <div class="container mt-5"> <!-- Agrega la clase 'container' de Bootstrap para centrar el contenido -->
      <div class="card">
        <div class="card-body">
          <h1 class="card-title">Lista de Cuentas de Administradores</h1>
          <ul class="list-group"> <!-- Usa la clase 'list-group' de Bootstrap para mostrar la lista -->
            <li v-for="admin in admins" :key="admin.id" class="list-group-item"> <!-- Cada elemento de la lista es un elemento de la lista -->
              {{ admin.first_name }} {{ admin.last_name }} - {{ admin.email }}
              <button @click="editarAdmin(admin)" class="btn btn-primary">Editar</button>
              <button @click="eliminarAdmin(admin.id)" class="btn btn-danger">Eliminar</button>
            </li>
          </ul>
        </div>
      </div>
    </div>
  </template>
  
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        admins: [], // Aquí almacenarás la lista de administradores
      };
    },
    created() {
      // Recupera el token del localStorage
      const TokenBearer = localStorage.getItem('sessionToken');
  
      // Verifica si hay un token
      if (TokenBearer) {
        // Realizar una solicitud HTTP al servidor con el token Bearer
        axios
          .get('http://127.0.0.1:8000/api/v1/user/?rol=administrador', {
            headers: {
              Authorization: `Bearer ${TokenBearer}`,
            },
          })
          .then((response) => {
            // Al recibir la respuesta del servidor, actualiza la lista de administradores
            this.admins = response.data;
          })
          .catch((error) => {
            console.error('Error al obtener la lista de administradores:', error);
          });
      } else {
        console.error('Token de autorización no encontrado en el localStorage');
        // Puedes redirigir al usuario al inicio de sesión si el token no está disponible
      }
    },/*
    methods: {
      editarAdmin(admin) {
        // Implementa la lógica para editar una cuenta de administrador
      },
      eliminarAdmin(adminId) {
        // Implementa la lógica para eliminar una cuenta de administrador
      },
    },*/
  };
  </script>
  
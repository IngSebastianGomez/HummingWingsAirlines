<template>
    <div class="container-sm mt-5">
      <h1>Iniciar Sesión</h1>
      <div class="container" style="padding-left: 4rem; padding-right: 4rem; padding-top: 2rem;">
        <form>
          <div class="mb-3">
            <label for="EmailAdmin" class="form-label">Correo electrónico</label>
            <input type="email" class="form-control" id="EmailAdmin" v-model="email">
          </div>
          <div class="mb-3">
            <label for="Password" class="form-label">Contraseña</label>
            <input type="password" class="form-control" id="Password" v-model="password">
          </div>
          <div class="d-grid gap-2 pb-5">
            <button class="btn btn-dark" type="button" style="background-color: #182a3f; border-radius: 40px;" @click="login">Ingresar</button>
          </div>
        </form>
      </div>
    </div>
  </template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      email: '',
      password: '',
    };
  },
  methods: {
    async login() {
      try {
        const requestData = {
          user: this.email,
          password: this.password,
          keep_logged_in: true,
          type: 'cliente',
        };

        const response = await axios.post('http://127.0.0.1:8000/api/v1/auth/', requestData);

        if (response.status >= 200 && response.status < 300) {
          // La solicitud fue exitosa (código de estado HTTP 2xx).
          // Realiza las acciones necesarias después del inicio de sesión exitoso.
          this.$router.push('/');
        } else {
          // La solicitud no fue exitosa (código de estado HTTP diferente de 2xx).
          console.error('Error en la solicitud:', response.status, response.data);
          // Puedes mostrar un mensaje de error al usuario o realizar otras acciones según el caso.
        }
      } catch (error) {
        // Maneja los errores, por ejemplo, muestra un mensaje de error al usuario.
        console.error('Error en la solicitud:', error);
      }
    },
  },
};
</script>

  
  <style>
    .container-sm{
      background: linear-gradient(114deg, #009D71 0%, rgba(0, 157, 117, 0.00) 100%);
      padding: 1rem;
      border-radius: 40px;
      margin-bottom: 2rem;
      max-width: 600px;
      box-shadow: 0 5px 10px rgba(71, 3, 6, 0.7);
    }
  </style>

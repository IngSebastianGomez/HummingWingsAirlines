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
        <router-link to="/RegistroUsuario" style="color: #182a3f;">¿No tienes cuenta? Regístrate</router-link>
      </form>
      <!-- Agrega un div para mostrar mensajes de error -->
      <div v-if="errorMessage" class="alert alert-danger" role="alert">
        {{ errorMessage }}
      </div>
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
      errorMessage: '', // Variable para mostrar mensajes de error
    };
  },
  methods: {
    async login() {
      const clientLogin = await this.tryLogin('cliente');

      if (clientLogin.success) {
        this.handleSuccessfulLogin(clientLogin.data);
      } else {
        const adminLogin = await this.tryLogin('administrador');

        if (adminLogin.success) {
          this.handleSuccessfulLogin(adminLogin.data);
        } else {
          // Ambos intentos de inicio de sesión fallaron.
          // Muestra un mensaje de error genérico.
          //this.errorMessage = 'Error en la solicitud. Por favor, intenta de nuevo más tarde.';
        }
      }
    },
    async tryLogin(role) {
      const requestData = {
        user: this.email,
        password: this.password,
        keep_logged_in: true,
        type: role,
      };

      try {
        const response = await axios.post('http://127.0.0.1:8000/api/v1/auth/', requestData);
        return {
          success: response.status >= 200 && response.status < 300,
          data: response.data,
        };
      } catch (error) {
        if (error.response.data && error.response.status === 401) {
          this.errorMessage = 'Contraseña incorrecta.';
        } else if (error.response.data && error.response.status === 400) {
          this.errorMessage = 'Usuario no encontrado o inactivo.';
        } else {
          // Error genérico.
          this.errorMessage = 'Usuario o contraseña incorrecto.';
        }

        return {
          success: false,
          error: error,
        };
      }
    },
    handleSuccessfulLogin(data) {
      // Actualiza los datos de Vuex con los datos de la respuesta
      this.$store.commit('setId', data.id);
      this.$store.commit('setUsername', data.email);
      this.$store.commit('setType', data.type);
      this.$store.commit('setToken', data.token);
      this.$store.commit('setRefresh', data.refresh);
      this.$store.commit('setEmail', data.email);
      this.$store.commit('setCellphone', data.cellphone);
      this.$store.commit('setFirstName', data.first_name);
      this.$store.commit('setLastName', data.last_name);
      this.$store.commit('setGender', data.gender);
      this.$store.commit('setRol', data.rol);
      this.$store.commit('setStatus', data.status);
      this.$store.commit('setDocument', data.document);
      this.$store.commit('setDocumentType', data.document_type);
      //poner loginLogged de vuex en true
      this.$store.commit('loginLogged', true);
      // Redirige al usuario a la página principal después del inicio de sesión exitoso
      this.$router.push('/');
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

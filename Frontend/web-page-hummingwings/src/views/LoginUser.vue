<template>
  <div class="container-sm mt-5">
    <h1>Iniciar Sesión</h1>
    <div class="container" style="padding-left: 4rem; padding-right: 4rem; padding-top: 2rem;">
      <form>
        <div class="mb-3">
          <label for="EmailAdmin" class="form-label">Correo electrónico</label>
          <input type="text" class="form-control" id="EmailAdmin" v-model="email" required>
        </div>
        <div class="mb-3">
          <label for="Password" class="form-label">Contraseña</label>
          <input type="password" class="form-control" id="Password" v-model="password" required>
        </div>
        <div class="d-grid gap-2 pb-5">
          <button v-if="!isAdminButtonVisible" class="btn btn-dark" type="button" style="background-color: #182a3f; border-radius: 40px;" @click="login">Ingresar</button>
          <button v-if="isAdminButtonVisible" class="admin-button" @click="AdLogin">Iniciar Sesión como Administrador</button>
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
      isAdminButtonVisible: false, // Variable para mostrar el botón de inicio de sesión de administrador
    };
  },
  created() {
    // Escucha el evento global de teclado
    window.addEventListener('keydown', this.handleKeyDown);
  },
  destroyed() {
    // Limpia el evento global de teclado cuando se destruye el componente
    window.removeEventListener('keydown', this.handleKeyDown);
  },
  methods: {
    handleKeyDown(event) {
      // Comprueba si se presiona Ctrl + Shift + U y si estamos en la ruta deseada
      if (event.ctrlKey && event.shiftKey && event.key === 'U' && this.$route.path === '/LoginUser') {
        this.isAdminButtonVisible = !this.isAdminButtonVisible;
      }
    },
    async login() {
  const clientLogin = await this.tryLogin('cliente');

  if (clientLogin && clientLogin.success) {
    this.handleSuccessfulLogin(clientLogin.data);
  } 
},

async AdLogin() {
  const adminLogin = await this.tryLogin('administrador');

  if (adminLogin && adminLogin.success) {
    this.handleSuccessfulLogin(adminLogin.data);
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
        if (response.status >= 200 && response.status < 300) {
      // La solicitud fue exitosa
      return {
        success: true,
        data: response.data,
      };
    } else {
      // La solicitud no fue exitosa
      this.errorMessage = 'Error en la solicitud. Por favor, intenta de nuevo más tarde.';
      console.error('Error en la solicitud. Código de estado:', response.status);
    }
  } catch (error) {
        // Error en la solicitud de red.
        this.errorMessage = `Ingresa los campos necesarios y correctos`;
        if (error.response && error.response.status === 401) {
          this.errorMessage = 'Clave incorrecta.';
        } else if (error.response && error.response.status === 404) {
          this.errorMessage = 'Usuario no registrado o inactivo.';
        }
        console.error('Error en la solicitud:', error);
      }
    },
    handleSuccessfulLogin(data) {
  if (data.status === 'pending') {
    // El estado es 'pending', muestra un mensaje o realiza alguna acción adicional
    this.errorMessage = 'Tu cuenta está pendiente de aprobación. Por favor, espera a que se active tu cuenta.';
  } else {
    // Actualiza los datos de Vuex y redirige al usuario a la página principal después del inicio de sesión exitoso
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
    // Poner loginLogged de Vuex en true
    this.$store.commit('loginLogged', true);
    // Redirige al usuario a la página principal después del inicio de sesión exitoso
    this.$router.push('/');
  }
}

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

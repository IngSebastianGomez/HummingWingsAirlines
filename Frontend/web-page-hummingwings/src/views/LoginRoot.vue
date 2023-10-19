<template>
  <div class="container-sm mt-5" style="background: linear-gradient(114deg, #881610 0%, #019970 100%);">
    <h1 class="myText">LoginRoot</h1>
    <div class="container" style="padding-left: 4rem; padding-top: 1rem;">
      <form>
        <div class="mb-3">
          <label for="username" class="form-label">Username</label><br>
          <input  class="form-control" id="username" placeholder="username" type="text" v-model="username">
        </div>
        <div class="mb-3">
          <label for="password" class="form-label">Password</label><br>
          <input class="form-control" id="password" placeholder="password" type="password" v-model="password">
        </div>
        <div class="d-grid gap-2 pb-5">
          <button class="btn btn-dark" type="button" style="background-color: #182a3f; border-radius: 40px;" @click="login">Login</button>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
// Importa Vuex y la mutación que definirás para actualizar el nombre de usuario
import { mapMutations } from 'vuex';

export default {
  data() {
    return {
      username: '',
      password: '',
    };
  },
  methods: {
    // Mapea la mutación que actualizará el nombre de usuario en Vuex
    ...mapMutations(['setUsername', 'setId', 'setType', 'setToken']), // Asegúrate de definir 'setUsername' en tu store
    
    async login() {
      try {
        const response = await axios.post('http://127.0.0.1:8000/api/v1/auth/', {
          user: this.username,
          password: this.password,
          keep_logged_in: true,
          type: 'root',
        });

        if (response.status >= 200 && response.status < 300) {
          // La solicitud fue exitosa (código de estado HTTP 2xx).
          
          // Después de recibir el token en la respuesta
          const token = response.data.token;
          localStorage.setItem('sessionToken', token);

          // Actualiza los datos de Vuex
          this.setUsername(response.data.username);
          this.setId(response.data.id);
          this.setType(response.data.type);
          //poner loginLogged de vuex en true
          this.$store.commit('loginLogged', true);
          

          // Redirige al usuario a la vista "opcionesRoot" después del inicio de sesión exitoso.
          this.$router.push('/opcionesRoot');
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

  
<style scoped>
  </style>
  
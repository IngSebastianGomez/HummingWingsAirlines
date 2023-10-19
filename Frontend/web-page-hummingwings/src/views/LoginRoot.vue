<template>
  <div class="container">
    <form @submit="login">
      <h1 class="title">LoginRoot</h1>
      <label>
        <i class="fa-solid fa-user"></i>
        <input placeholder="username" type="text" v-model="username">
      </label>
      <label>
        <i class="fa-solid fa-lock"></i>
        <input placeholder="password" type="password" v-model="password">
      </label>
      <button type="submit">Login</button>
    </form>
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
  .container {
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 100vh; /* Usar min-height en lugar de height */
    background-color: red; /* Cambiar el color de fondo aquí */
  }
  
  form {
    text-align: center;
    padding: 20px 25px;
    box-shadow: 0 5px 10px rgba(71, 3, 6, 0.7);
    width: 300px; /* Ajusta el ancho del formulario según tus necesidades */
    background: #fff;
  }
  
  form .title {
    color: #252525;
    font-size: 35px;
    font-weight: 800;
    margin-bottom: 30px;
  }
  
  form label {
    margin-bottom: 20px; /* Reducir el espacio entre etiquetas */
  }
  
  form label .fa-solid {
    font-size: 20px;
    color: #cb232c;
    margin-right: 10px;
  }
  
  form label input {
    outline: none;
    border: none;
    color: #252525;
    border-bottom: solid 1px #ce1d61;
    padding: 0 5px;
    font-size: 18px;
  }
  
  form label input::placeholder {
    color: rgba(37, 37, 37, 0.5);
  }
  
  form .link {
    color: #252525;
    margin-bottom: 15px;
  }
  
  form button {
    color: #fff;
    border: none;
    background: linear-gradient(to right, #cb232c, #ce1d61);
    padding: 10px 15px;
    cursor: pointer;
    font-size: 20px;
  }
  </style>
  
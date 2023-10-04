<template>
    <div>
        <RouterLink to="/">Home</RouterLink>

      <h2>Formulario de Inicio de Sesión</h2>
  
      <form @submit="handleSubmit">
        <div>
          <label for="username">Usuario:</label>
          <input
            type="text"
            id="username"
            v-model="username"
            required
          />
        </div>
  
        <div>
          <label for="password">Contraseña:</label>
          <input
            type="password"
            id="password"
            v-model="password"
            required
          />
        </div>
  
        <div>
          <button type="submit">Iniciar Sesión</button>
        </div>
      </form>
  
      <!-- Mostrar mensaje de error si hay un error de autenticación -->
      <div v-if="error" class="error-message">{{ error }}</div>
    </div>
  </template>
  
  <script>
  import axios from "axios";
  
  export default {
    data() {
      return {
        username: "",
        password: "",
        error: null,
      };
    },
    methods: {
      handleSubmit(event) {
        event.preventDefault(); // Evita que el formulario se envíe
  
        // Accede a los valores de usuario y contraseña desde data
        const username = this.username;
        const password = this.password;
  
        // Realiza una solicitud POST a un servidor para validar el usuario y la contraseña
        axios
          .post("/api/login", {
            username,
            password,
          })
          .then((response) => {
            // Aquí puedes manejar la respuesta del servidor
            console.log("Respuesta del servidor:", response.data);
  
            // Restablecer los valores de usuario y contraseña si es necesario
            this.username = "";
            this.password = "";
            this.error = null; // Limpia cualquier mensaje de error anterior
          })
          .catch((error) => {
            // Manejar errores de la solicitud
            console.error("Error:", error);
            this.error = "Error de autenticación"; // Puedes mostrar un mensaje de error al usuario
          });
      },
    },
  };
  </script>
  
  <style>
  /* Estilos CSS personalizados aquí */
  </style>
  
<style scoped>
.error-message {
    color: aliceblue;
    margin-top: 20px;
    border: 1px solid #ccc;
    padding: 20px;
}
</style>

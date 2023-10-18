<template>
    <div class="container">
      <form action="">
        <h1 class="title">LoginRoot</h1>
        <label>
          <i class="fa-solid fa-user"></i>
          <input placeholder="username" type="text" id="username">
        </label>
        <label>
          <i class="fa-solid fa-lock"></i>
          <input placeholder="password" type="password" id="password">
        </label>
        <button id="button">Login</button>
      </form>
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
  
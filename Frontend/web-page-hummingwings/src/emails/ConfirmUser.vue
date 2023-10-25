<template>
    <div class="confirmation-page">
      <div class="container">
        <h2>Confirmación de Registro</h2>
        <p>Gracias por registrarte en nuestro sitio web. Para completar tu registro, por favor confirma tu dirección de correo electrónico:</p>
        <p>Haz clic en el siguiente botón para confirmar tu registro:</p>
        <button class="button" @click="confirmarRegistro">Confirmar Registro</button>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    methods: {
      confirmarRegistro() {
        const { pk, token } = this.$route.params; // Obtén id y token de la URL
        const url = `http://127.0.0.1:8000/api/v1/user/${pk}/confirm_email/${token}`;
        const jsonData = {
          is_admin: true
        };
  
        // Realiza la solicitud PATCH con los datos JSON
        fetch(url, {
          method: 'PATCH',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify(jsonData),
        })
        .then(response => {
          if (response.status === 200) {
            // Redirige a la página principal si la respuesta es un código 200
            this.$router.push('/');
          } else {
            // La solicitud fue exitosa pero no es un código 200, puedes manejarlo según tus necesidades
            console.log('Respuesta exitosa pero no es un código 200:', response);
          }
          })
          .catch(error => {
            // Ocurrió un error, maneja el error aquí
            console.error('Error en la solicitud:', error);
          });
      },
    },
  };
  </script>
  
  <style scoped>
  .confirmation-page {
    display: flex;
    align-items: center;
    justify-content: center;
    height: 100vh;
  }
  
  .container {
    max-width: 600px;
    padding: 20px;
    background-color: #fff;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    text-align: center;
  }
  
  h2 {
    color: #333;
  }
  
  p {
    color: #666;
  }
  
  .button {
    display: inline-block;
    padding: 10px 20px;
    background-color: #182a3f;
    color: #fff;
    text-decoration: none;
    border-radius: 40px;
    cursor: pointer;
  }
  </style>
  
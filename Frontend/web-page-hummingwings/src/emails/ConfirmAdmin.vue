<template>
  <div>
    <div class="container-sm mt-5">
      <h2>Rellena los campos para terminar el registro</h2>

      <form @submit.prevent="enviarFormulario">
        <div class="mb-3">
          <label for="exampleInputName1" class="form-label">Nombre</label>
          <input type="text" class="form-control" id="exampleInputName1" v-model="formData.first_name" required/>
        </div>

        <div class="mb-3">
          <label for="exampleInputLastName1" class="form-label">Apellido</label>
          <input type="text" class="form-control" id="exampleInputLastName1" v-model="formData.last_name" required/>
        </div>

        <div class="mb-3">
          <label for="birthday" class="form-label">Fecha de Nacimiento</label>
          <input type="date" class="form-control" id="birthday" min="1924-01-01" max="2022-10-15" v-model="formData.birth_date" required/>
        </div>

        <div class="mb-3">
          <label for="gender" class="form-label">Género</label>
          <select class="form-select" v-model="formData.gender">
            <option value="" disabled selected>Género</option>
            <option value="masculino">masculino</option>
            <option value="femenino">femenino</option>
            <option value="otro">Prefiero no decirlo</option>
          </select>
        </div>

        <div class="mb-3">
          <label for="InputPhoneNumber" class="form-label">Número de teléfono</label>
          <input type="text" class="form-control" id="InputPhoneNumber" v-model="formData.cellphone" required @blur="validarNumber"/>
        </div>

        <!-- Agregar campo para dirección de residencia -->
        <div class="mb-3">
          <label for="InputAddress" class="form-label">Dirección de Residencia</label>
          <input type="text" class="form-control" id="InputAddress" v-model="formData.address" required/>
        </div>

        <div class="d-grid gap-2 pb-5">
          <button class="btn btn-primary" type="button">Subir foto de perfil</button>
          <button class="btn btn-dark" v-if="!showSuccessAlert" type="submit" style="background-color: #182a3f; border-radius: 40px;">Enviar</button>
        </div>

        <!-- Alerta de aprobación (éxito) -->
    <div v-if="showSuccessAlert" class="alert alert-success" role="alert">
      Aprobación realizada con éxito.
      <button @click="redirigirAlInicio" class="btn btn-primary">Ir al inicio</button>
    </div>
    
    <!-- Alerta de error -->
    <div v-if="showErrorAlert" class="alert alert-danger" role="alert">
      No se pudo realizar la solicitud.
    </div>
      </form>
    </div>
    
  </div>
</template>

<!-- El script permanece igual -->
<script>
import axios from 'axios';

const BASE_URL = 'http://127.0.0.1:8000/api/v1/admin/';
//const DEFAULT_EMAIL = 'admin7@yopmail.com';  // Cambia esto a tu valor predeterminado

export default {
  data() {
    return {
      formData: {
        address: '',
        birth_date: '',
        cellphone: '',
        first_name: '',
        gender: '',
        last_name: ''
      },
      showSuccessAlert: false, // Mostrar mensaje de aprobación
      showErrorAlert: false,   // Mostrar mensaje de error
      statusCode: null,       // Código de respuesta del servidor
    };
  },
  methods: {
    redirigirAlInicio() {
      this.$router.push('/');
    },
    validarNumber() {
      const telefono = this.formData.cellphone;
      const soloDigitos = /^\d+$/; // Expresión regular para verificar que solo hay dígitos

      if (telefono && !soloDigitos.test(telefono)) {
        this.errorMessage = 'El número solo debe contener dígitos.';
      } else if (telefono && telefono.length < 10) {
        this.errorMessage = 'El número debe tener al menos 10 dígitos.';
      } else {
        this.errorMessage = ''; 
      }
    },
    enviarFormulario() {
  const { pk, token } = this.$route.params;  // Obtén pk y token de la URL
  const url = `${BASE_URL}${pk}/confirm_email/${token}`;

  // Realiza la solicitud PATCH con los datos del formulario
  axios.patch(url, this.formData)
    .then(response => {
      // Verifica si la respuesta es válida antes de acceder a 'status'
      if (response) {
        // La solicitud fue exitosa, puedes manejar la respuesta aquí
        // Guarda el código de respuesta
        this.showSuccessAlert = true; // Muestra el mensaje de aprobación
        this.showErrorAlert = false;  // Oculta el mensaje de error
        // Redirige a donde sea necesario
      } else {
        // La respuesta es inválida, puedes manejarla aquí
        // Esto podría ser un error de servidor o una respuesta vacía
      }
    })
    .catch(error => {
      // Ocurrió un error, maneja el error aquí
      if (error.response) {
         // Guarda el código de respuesta del error
      } else {
        // Puede manejar otros tipos de errores aquí si error.response no está disponible
      }
      this.showErrorAlert = true; // Muestra el mensaje de error
    });
}

    
  }
}
</script>
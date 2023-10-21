<template>
  <div>
    <p>Parámetro 'pk': {{ $route.params.pk }}</p>
    <p>Parámetro 'token': {{ $route.params.token }}</p>

    <div class="container-sm mt-5">
      <h2>Rellena los campos para terminar el registro</h2>

      <form @submit.prevent="enviarFormulario">
        <div class="mb-3">
          <label for="exampleInputName1" class="form-label">Nombre</label>
          <input type="text" class="form-control" id="exampleInputName1" v-model="formData.first_name" />
        </div>

        <div class="mb-3">
          <label for="exampleInputLastName1" class="form-label">Apellido</label>
          <input type="text" class="form-control" id="exampleInputLastName1" v-model="formData.last_name" />
        </div>

        <div class="mb-3">
          <label for="birthday" class="form-label">Fecha de Nacimiento</label>
          <input type="date" class="form-control" id="birthday" min="1924-01-01" max="2022-10-15" v-model="formData.birth_date" />
        </div>

        <div class="mb-3">
          <label for="gender" class="form-label">Género</label>
          <select class="form-select" v-model="formData.gender">
            <option value="" disabled selected>Género</option>
            <option value="masculino">masculino</option>
            <option value="femenino">femenino</option>
            <option value="Prefiero no decirlo">Prefiero no decirlo</option>
          </select>
        </div>

        <div class="mb-3">
          <label for="InputPhoneNumber" class="form-label">Número de teléfono</label>
          <input type="text" class="form-control" id="InputPhoneNumber" v-model="formData.cellphone" />
        </div>

        <!-- Agregar campo para dirección de residencia -->
        <div class="mb-3">
          <label for="InputAddress" class="form-label">Dirección de Residencia</label>
          <input type="text" class="form-control" id="InputAddress" v-model="formData.address" />
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
const DEFAULT_EMAIL = 'admin6@yopmail.com';  // Cambia esto a tu valor predeterminado

export default {
  data() {
    return {
      formData: {
        address: '',
        birth_date: '',
        cellphone: '',
        email: DEFAULT_EMAIL,
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
    enviarFormulario() {
      const { pk, token } = this.$route.params;  // Obtén pk y token de la URL
      const url = `${BASE_URL}${pk}/confirm_email/${token}`;

      // Realiza la solicitud PATCH con los datos del formulario
      axios.patch(url, this.formData)
        .then(response => {
          // La solicitud fue exitosa, puedes manejar la respuesta aquí
          this.statusCode = response.status; // Guarda el código de respuesta
          this.showSuccessAlert = true; // Muestra el mensaje de aprobación
          // Redirige a donde sea necesario
        })
        .catch(error => {
          // Ocurrió un error, maneja el error aquí
          this.statusCode = error.response.status; // Guarda el código de respuesta del error
          this.showErrorAlert = true; // Muestra el mensaje de error
        });
        
    }
    
  }
}
</script>
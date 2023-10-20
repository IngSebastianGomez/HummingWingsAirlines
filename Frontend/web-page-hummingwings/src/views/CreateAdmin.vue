<template>
  <div class="container-sm mt-5 degradade-root" style="background: linear-gradient(114deg, #881610 0%, #019970 100%);">
    <h1>Crear usuario administrador</h1>
    <div class="container" style="padding-left: 4rem; padding-right: 4rem; padding-top: 2rem;">
      <form @submit.prevent="crearUsuario">
        <div class="mb-3">
          <label for="EmailAdmin" class="form-label">Correo electrónico</label>
          <input type="email" class="form-control" id="EmailAdmin" v-model="email">
        </div>
        <div class="mb-3">
          <label for="Password" class="form-label">Contraseña</label>
          <input type="password" class="form-control" id="Password" v-model="password">
        </div>
        <div class="mb-3">
          <label for="identityDocument" class="form-label">Documento de identidad</label>
          <select id="identityDocument" class="form-select" aria-label="Default select example" v-model="document_type">
            <option selected>Documento de identidad</option>
            <option value="C.C.">Cédula de Ciudadanía</option>
            <option value="Pasaporte">Pasaporte</option>
          </select>
        </div>
        <div class="mb-3">
          <label for="exampleInputNumeroIdentificacion1" class="form-label">Número de identificación</label>
          <input type="text" class="form-control" id="exampleInputNumeroIdentificacion1" v-model="document">
        </div>
        <div class="d-grid gap-2 pb-5">
          <button class="btn btn-dark" type="submit" style="background-color: #182a3f; border-radius: 40px;" v-if="!insertedAccountId">Crear</button>
        </div>
      </form>
    </div>

    <!-- Mensaje de error -->
    <div v-if="showErrorMessage" class="alert alert-danger">
      Admin ya existente 
    </div>

    <!-- Mensaje de ID de cuenta insertado -->
    <div v-if="insertedAccountId" class="alert alert-success">
      Cuenta creada con éxito. ID de cuenta: {{ insertedAccountId }} <button type="button" class="btn btn-primary float-right" @click="redirigirAtras">OK</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      email: 'admin5@yopmail.com',
      password: 'admin123',
      document_type: 'C.C.',
      document: '1059709215',
      showSuccessMessage: false,
      showErrorMessage: false,
      insertedAccountId: null, // Variable para mostrar el ID de la cuenta insertada
    };
  },
  methods: {
    async crearUsuario() {
      const requestData = {
        email: this.email,
        document_type: this.document_type,
        document: this.document,
        password: this.password,
      };

      const config = {
        headers: {
          Authorization: `Bearer ${this.$store.state.token}`,
        },
      };

      try {
        const response = await axios.post('http://127.0.0.1:8000/api/v1/admin/', requestData, config);

        if (response.data.inserted) {
          // Muestra el mensaje con el ID de cuenta insertado
          this.insertedAccountId = response.data.inserted;
          this.showSuccessMessage = true;
          this.showErrorMessage = false;
        }
      } catch (error) {
        if (error.response && error.response.data.code === "integrity_error") {
          this.showErrorMessage = true;
        } else {
          console.error('Error al crear usuario administrador:', error);
        }
      }
    },
    redirigirAtras() {
      this.showSuccessMessage = false;
      this.showErrorMessage = false;
      this.$router.go(-1);
    },
  },
};
</script>

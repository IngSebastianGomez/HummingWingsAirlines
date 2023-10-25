<template>
  <div class="container-sm mt-5 degradade-root" style="background: linear-gradient(114deg, #881610 0%, #019970 100%);">
    <h1>Crear usuario administrador</h1>
    <div class="container" style="padding-left: 4rem; padding-right: 4rem; padding-top: 2rem;">
      <form @submit.prevent="crearUsuario">
        <div class="mb-3">
          <label for="EmailAdmin" class="form-label">Correo electrónico</label>
          <input type="email" class="form-control" id="EmailAdmin" v-model="email" required @blur="validarEmail">
        </div>
        <div class="mb-3">
          <label for="Password" class="form-label">Contraseña</label>
          <input type="password" class="form-control" id="Password" v-model="password" required @blur="validarContrasena">
        </div>
        <div class="mb-3">
          <label for="ConfirmPassword" class="form-label">Confirmar Contraseña</label>
          <input type="password" class="form-control" id="ConfirmPassword" v-model="confirmPassword" required @blur="validarConfirmacionContrasena">
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
          <input type="text" min="0" class="form-control" id="exampleInputNumeroIdentificacion1" v-model="document" required @blur="validarDocNumber">
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
    <div v-if="errorMessage" class="alert alert-danger" role="alert">
      {{ errorMessage }}
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
      confirmPassword: '', // Campo de confirmación de contraseña
      document_type: '',
      document: '',
      showSuccessMessage: false,
      showErrorMessage: false,
      insertedAccountId: null, // Variable para mostrar el ID de la cuenta insertada
    };
  },
  methods: {
    async crearUsuario() {
      // Validar la contraseña y la confirmación de contraseña
      if (this.password.length < 7) {
        this.errorMessage = 'La contraseña debe tener al menos 7 caracteres.';
        return;
      }
      if (this.password !== this.confirmPassword) {
        this.errorMessage = 'Las contraseñas no coinciden. Por favor, inténtalo de nuevo.';
        return;
      }

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
    validarDocNumber() {
      const document = this.document;
      const soloDigitos = /^\d+$/; // Expresión regular para verificar que solo hay dígitos

      if (document && !soloDigitos.test(document)) {
        this.errorMessage = 'El número de documento solo debe contener dígitos.';
      } else {
        this.errorMessage = ''; 
      }
    },
    validarContrasena() {
      if (this.password.length >= 7) {
        // Restablecer el mensaje de error si la contraseña es válida
        this.errorMessage = '';
      } else {
        this.errorMessage = "Contraseña inválida"
      }
    },
    validarConfirmacionContrasena() {
      if (this.confirmPassword.length < 7) {
        this.errorMessage = 'La confirmación de contraseña debe tener al menos 7 caracteres.';
      } else if (this.password !== this.confirmPassword) {
        this.errorMessage = 'Las contraseñas no coinciden. Por favor, inténtalo de nuevo.';
      } else {
        this.errorMessage = ''; 
      }
    },
    validarEmail() {
      const email = this.email;
      const regex = /^(?!.*\.\.)(?!.*@.*\.\.)(?!.*\.$)[a-zA-Z0-9._-]*[a-zA-Z0-9]+(\.[a-zAZ0-9]+)*@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}/;
      if (regex.test(email) == false) {
        this.errorMessage = 'Email no válido';
      } else {
        this.errorMessage = '';
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


<template>
  <div class="container-sm mt-5">
    <form @submit="enviarFormulario">
      <div class="mb-3">
        <label for="exampleInputName1" class="form-label">Nombre</label>
        <input type="text" class="form-control" id="exampleInputName1" v-model="formData.first_name" required>
      </div>

      <div class="mb-3">
        <label for="exampleInputLastName1" class="form-label">Apellido</label>
        <input type="text" class="form-control" id="exampleInputLastName1" v-model="formData.last_name" required>
      </div>

      <div class="mb-3">
        <label for="identityDocument" class="form-label">Documento de identidad</label>
        <select class="form-select" v-model="formData.document_type" required>
          <option value="" disabled selected>Documento de identidad</option>
          <option value="C.C.">C.C.</option>
          <option value="Pasaporte">Pasaporte</option>
        </select>
      </div>

      <div class="mb-3">
        <label for="exampleInputNumeroIdentificacion1" class="form-label">Número de identificación</label>
        <input type="text" min="0" class="form-control" id="exampleInputNumeroIdentificacion1" v-model="formData.document" required
          @blur="validarDocNumber">
      </div>

      <div class="mb-3">
        <label for="birthday" class="form-label">Fecha de Nacimiento</label>
        <input type="date" class="form-control" id="birthday" v-model="formData.birth_date" min="1924-01-01"
          max="2022-10-15" required>
      </div>

      <div class="mb-3">
        <label for="gender" class="form-label">Género</label>
        <select class="form-select" v-model="formData.gender" required>
          <option value="" disabled selected>Género</option>
          <option value="masculino">masculino</option>
          <option value="femenino">femenino</option>
          <option value="otro">Prefiero no decirlo</option>
        </select>
      </div>

      <div class="mb-3">
        <label for="InputPhoneNumber" class="form-label">Número de teléfono (debe tener al menos 10 dígitos)</label>
        <input type="text" min="0" class="form-control" id="InputPhoneNumber" v-model="formData.cellphone" required
          @blur="validarNumber">
      </div>

      <div class="mb-3">
        <label for="exampleInputEmail1" class="form-label">Correo Electrónico (debe ser una dirección de correo
          válida)</label>
        <input type="email" class="form-control" id="exampleInputEmail1" v-model="formData.email" required>
      </div>

      <div class="mb-3">
        <label for="exampleInputPassword1" class="form-label">Contraseña (debe tener al menos 7 caracteres)</label>
        <input type="password" class="form-control" id="exampleInputPassword1" v-model="formData.password" required
          @blur="validarContrasena">
        <div v-if="errorMessage" class="alert alert-danger" role="alert">
          {{ errorMessage }}
        </div>
      </div>

      <div class="d-grid gap-2 pb-5">
        <button class="btn btn-primary" type="button">Subir foto de perfil</button>
        <button class="btn btn-dark" type="submit" style="background-color: #182a3f; border-radius: 40px;">Enviar</button>
      </div>
    </form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      formData: {
        address: "Mz 4 Cs 2",
        birth_date: "1990-01-07",
        cellphone: "3233123323",
        document: "103213213",
        email: "sebax@yopmail.com",
        first_name: "Sebastian",
        gender: "masculino",
        last_name: "Gonzalez",
        password: "humming23",
        rol: "cliente",
        document_type: "C.C.",
      },
    };
  },
  methods: {
    enviarFormulario() {
      // Validar la contraseña antes de enviar el formulario
      if (this.formData.password.length < 7) {
        this.errorMessage = 'La contraseña debe tener al menos 7 caracteres.';
        return;
      }

      // Resto del código para enviar el formulario
      // ...

      axios.post('http://127.0.0.1:8000/api/v1/user/', this.formData)
        .then((response) => {
          // Redirigir a otra página o realizar otras acciones según el caso
          this.$router.push('/');
          console.log("Formulario enviado con éxito:", response.data);
        })
        .catch((error) => {
          // Manejar errores de la solicitud al servidor
          console.error("Error al enviar el formulario:", error);
          // Mostrar un mensaje de error al usuario o realizar otras acciones según el caso
        });
    },

    validarContrasena() {
      if (this.formData.password.length >= 7) {
        // Restablecer el mensaje de error si la contraseña es válida
        this.errorMessage = '';
      }
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
    validarDocNumber() {
      const document = this.formData.document;
      const soloDigitos = /^\d+$/; // Expresión regular para verificar que solo hay dígitos

      if (document && !soloDigitos.test(document)) {
        this.errorMessage = 'El número de documento solo debe contener dígitos.';
      } else {
        this.errorMessage = ''; 
      }
    },
  },
};
</script>

<style>
.container-sm {
  background: linear-gradient(112deg, #009D71 20.89%, rgba(0, 157, 117, 0.00) 89.16%);
  border-radius: 40px;
  padding: 1rem;
}

body {
  background-color: #171A4A;
}</style>

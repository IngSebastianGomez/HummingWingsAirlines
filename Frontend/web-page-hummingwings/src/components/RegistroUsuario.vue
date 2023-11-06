<template>
  <div class="container-sm mt-5">
    <form @submit="enviarFormulario">
      <div class="mb-3">
        <label for="InputName1" class="form-label">Primer nombre</label>
        <input type="text" class="form-control" id="InputName1" v-model="formData.first_name" required
        @blur="validarNombre">
      </div>
      <div v-if="errorName" class="alert alert-danger" role="alert">
        El nombre no puede contener espacios en blanco ni al inicio ni al final.
      </div>

      <div class="mb-3">
        <label for="InputLastName1" class="form-label">Primer apellido</label>
        <input type="text" class="form-control" id="InputLastName1" v-model="formData.last_name" required
        @blur="validarApellido">
      </div>
      <div v-if="errorLastName" class="alert alert-danger" role="alert">
        El apellido no puede contener espacios en blanco ni al inicio ni al final.
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

      <div v-if="errorDocument" class="alert alert-danger" role="alert">
        El número de documento solo debe contener dígitos.
      </div>

      <div class="mb-3">
        <label for="birthday" class="form-label">Fecha de Nacimiento</label>
        <input type="date" class="form-control" id="birthday" v-model="formData.birth_date" min="1924-01-01"
          max="2004-10-15" required>
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

      <div v-if="errorTel" class="alert alert-danger" role="alert">
          {{ errorMessage }}
      </div>

      <div class="mb-3">
        <label for="exampleInputEmail1" class="form-label">Correo Electrónico (debe ser una dirección de correo
          válida)</label>
        <input type="email" class="form-control" id="exampleInputEmail1" v-model="formData.email" required>
      </div>

      <div class="mb-3">
        <label for="exampleInputPassword1" class="form-label">Contraseña (debe tener al menos 7 caracteres)</label>
        <div class="input-group">
          <input :type="showPassword ? 'text' : 'password'" class="form-control" id="exampleInputPassword1" v-model="formData.password" required @blur="validarContrasena">
          <span class="input-group-text" @click="togglePasswordVisibility">
            <i class="fas" :class="showPassword ? 'fa-eye' : 'fa-eye-slash'"></i>
          </span>
        </div>
      </div>

      <div v-if="errorLenPass" class="alert alert-danger" role="alert">
        La contraseña debe tener al menos 7 caracteres.
      </div>

      <div class="mb-3">
        <label for="exampleInputPassword2" class="form-label">Confirmar Contraseña</label>
        <input type="password" class="form-control" id="exampleInputPassword2" v-model="confirmPassword" required @blur="validarConfirmacionContrasena">
      </div>
      
      <div v-if="errorDiferPass" class="alert alert-danger" role="alert">
        Las contraseñas no coinciden. Por favor, inténtalo de nuevo.
        </div>
      <div class="mb-3">
        <label for="exampleInputAddress" class="form-label">Dirección</label>
        <input type="text" class="form-control" id="exampleInputAddress" v-model="formData.address" required>
      </div>
      <div class="d-grid gap-2 pb-5">
        <button class="btn btn-primary" type="button">Subir foto de perfil</button>
        <button class="btn btn-dark" type="submit" style="background-color: #182a3f; border-radius: 40px;" @click="enviarFormulario">Enviar</button>
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
        address: "",
        birth_date: "",
        cellphone: "",
        document: "",
        email: "",
        first_name: "",
        gender: "",
        last_name: "",
        password: "",
        rol: "cliente",
        document_type: "",
      },
      confirmPassword: "", // Nueva propiedad para la confirmación de la contraseña
      errorMessage: "", // Variable para mostrar mensajes de error
      errorDocument: false, //Verifica si hubo un error con el numero de documento
      errorLenPass: false, //Verifica si hubo error con el largo de la contraseña
      errorDiferPass: false, //Verifica si los dos campos de contraseña son diferentes
      errorTel: false, //Verifica si hubo error con el numero de telefono
      errorName: false, //Verifica que el primer nombre no sea espacios en blanco
      errorLastName: false, //Verifica que el apellido no sea espacios en blanco
    };
  },
  methods: {
    enviarFormulario() {
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
      // Validar la longitud de la contraseña
      if (this.formData.password.length < 7) {
          this.errorLenPass= true;
          return;
        } else {
          this.errorLenPass = false;
        }
      },

    validarConfirmacionContrasena(){
        // Validar la confirmación de contraseña
      if (this.formData.password !== this.confirmPassword) {
          this.errorDiferPass = true;
          return;
        } else{
          this.errorDiferPass = false;
        }
      
    },

    validarNumber() {
      const telefono = this.formData.cellphone;
      const soloDigitos = /^\d+$/; // Expresión regular para verificar que solo hay dígitos

      if (telefono && !soloDigitos.test(telefono)) {
        this.errorMessage = 'El número solo debe contener dígitos.';
        this.errorTel= true;
      } else if (telefono && telefono.length < 10) {
        this.errorMessage = 'El número debe tener al menos 10 dígitos.';
        this.errorTel = true;
      } else {
        this.errorMessage = '';
        this.errorTel = false;
      }
    },
    validarDocNumber() {
      const document = this.formData.document;
      const soloDigitos = /^\d+$/; // Expresión regular para verificar que solo hay dígitos

      if (!soloDigitos.test(document)) {
        this.errorDocument = true;
      } else {
        this.errorDocument = false;
      }
    },
    validarNombre() {
      const nombreAValidar = this.formData.first_name;
      //Expresion regular para que no hayan espacios en blanco ni al inicio ni al final de la cadena
      const sinEspacios = /^(?!\s)(.*\S)(?!\s)*$/;
      if(nombreAValidar && !sinEspacios.test(nombreAValidar)){
        this.errorName = true;
      } else {
        this.errorName = false;
      }
    },
    validarApellido() {
      const nombreAValidar = this.formData.last_name;
      const sinEspacios = /^(?!\s)(.*\S)(?!\s)*$/;
      if(nombreAValidar && !sinEspacios.test(nombreAValidar)){
        this.errorLastName = true;
      } else {
        this.errorLastName = false;
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

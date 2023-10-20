<template>
  <div class="container-sm mt-5">
    <form @submit="enviarFormulario">
      <div class="mb-3">
        <label for="exampleInputName1" class="form-label">Nombre</label>
        <input type="text" class="form-control" id="exampleInputName1" v-model="formData.first_name">
      </div>

      <div class="mb-3">
        <label for="exampleInputLastName1" class="form-label">Apellido</label>
        <input type="text" class="form-control" id="exampleInputLastName1" v-model="formData.last_name">
      </div>

      <div class="mb-3">
        <label for="identityDocument" class="form-label">Documento de identidad</label>
        <select class="form-select" v-model="formData.document_type">
          <option value="" disabled selected>Documento de identidad</option>
          <option value="C.C.">C.C.</option>
          <option value="Pasaporte">Pasaporte</option>
        </select>
      </div>

      <div class="mb-3">
        <label for="exampleInputNumeroIdentificacion1" class="form-label">Número de identificación</label>
        <input type="text" class="form-control" id="exampleInputNumeroIdentificacion1" v-model="formData.document">
      </div>

      <div class="mb-3">
        <label for="birthday" class="form-label">Fecha de Nacimiento</label>
        <input type="date" class="form-control" id="birthday" v-model="formData.birth_date" min="1924-01-01" max="2022-10-15">
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
        <label for="InputPhoneNumber" class="form-label">Número de teléfono</label> <!-- Aqui hay que poner una condicion para que tenga minimo 10 digitos -->
        <input type="text" class="form-control" id="InputPhoneNumber" v-model="formData.cellphone">
      </div>

      <div class="mb-3">
        <label for="exampleInputEmail1" class="form-label">Correo Electrónico</label>
        <input type="email" class="form-control" id="exampleInputEmail1" v-model="formData.email">
      </div>

      <div class="mb-3">
        <label for="exampleInputPassword1" class="form-label">Contraseña</label>
        <input type="password" class="form-control" id="exampleInputPassword1" v-model="formData.password">
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
        document_type: "C.C."
      },
    };
  },
  methods: {
    enviarFormulario() {
      // Aquí puedes realizar una solicitud POST a tu servidor utilizando Axios o Fetch
      // Ejemplo usando Axios:
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
  },
};
</script>

<style>
  .container-sm{
    background: linear-gradient(112deg, #009D71 20.89%, rgba(0, 157, 117, 0.00) 89.16%);
    border-radius: 40px;
    padding: 1rem;
  }
  body{
    background-color: #171A4A;
  }
</style>
<template>
  <div class="container-sm mt-5 degradade-root" style="background: linear-gradient(114deg, #881610 0%, #019970 100%);">
    <h1>Crear usuario administrador</h1>
    <div class="container" style="padding-left: 4rem; padding-right: 4rem; padding-top: 2rem;">
      <form @submit.prevent="crearUsuario">
        <div class="mb-3">
          <label for="EmailAdmin" class="form-label">Correo electronico</label>
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
          <button class="btn btn-dark" type="submit" style="background-color: #182a3f; border-radius: 40px;" >Crear</button>
        </div>
      </form>
    </div>
    <!-- Button trigger modal -->
<button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#exampleModal">
  Launch demo modal
</button>

<!-- Modal -->
<div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="exampleModalLabel">Modal title</h5>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="modal-body">
        ...
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
        <button type="button" class="btn btn-primary" @click="guardarCambiosYVolverAtras">Save changes</button>
      </div>
    </div>
  </div>
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
      showSuccessMessage: false, // Agregamos una variable para controlar la visibilidad del mensaje de éxito
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

    // Mostrar la ventana modal de éxito sin importar el resultado
    //this.showSuccessMessage = true;

    try {
      await axios.post('http://127.0.0.1:8000/api/v1/admin/', requestData, config);

      // Muestra la ventana modal de éxito en caso de éxito
      this.showSuccessMessage = true;
    } catch (error) {
      // Manejar errores, por ejemplo, mostrar un mensaje de error al usuario.
      console.error('Error al crear usuario administrador:', error);
    }
  },
    redirigirAtras() {
      // Redirige al usuario a la página anterior con el enrutador
      this.showSuccessMessage = false; // Oculta la ventana modal antes de redirigir
      this.$router.go(-1);
    },
  },
};
</script>


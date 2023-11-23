<template>
  <div class="container-sm mt-5 mb-5">
    <h1 style="text-align: center;">Agregar Vuelo</h1><br>
    <form @submit="enviarFormulario">
      <div class="mb-3">
        <label for="inputPlate" class="form-label">Placa Vuelo</label>
        <input type="text" class="form-control" id="inputPlate" v-model="formData.plate" required
        @blur="validarPlaca">
      </div>
      <div v-if="errorPlate" class="alert alert-danger" role="alert">
        {{ errorPlate }}
      </div>

      <div class="mb-3">
        <label for="inputOrigin" class="form-label">Origen Vuelo</label>
        <input type="text" class="form-control" id="inputOrigin" v-model="formData.origin" required
        @blur="validarOrigen">
      </div>

      <div v-if="errorOrigin" class="alert alert-danger" role="alert">
        {{ errorOrigin }}
      </div>

      <div class="mb-3">
        <label for="inputDestiny" class="form-label">Destino Vuelo</label>
        <input type="text" class="form-control" id="inputDestiny" v-model="formData.destiny" required
        @blur="validarDestino">
      </div>

      <div v-if="errorDestiny" class="alert alert-danger" role="alert">
        {{ errorDestiny }}
      </div>

      <div class="mb-3">
        <label for="flightDate" class="form-label">Fecha de Vuelo</label>
        <input type="date" class="form-control" id="flightDate" v-model="formData.flight_date"
        min="2023-11-05" max="2025-12-31" required>
      </div>

      <div v-if="errorDate" class="alert alert-danger" role="alert">
        {{ errorDate }}
      </div>

      <div class="mb-3">
        <label for="inputTime" class="form-label">Hora de Vuelo</label>
        <input type="text" class="form-control" id="inputTime" v-model="formData.time" required
        @blur="validarHora">
      </div>

      <div v-if="errorTime" class="alert alert-danger" role="alert">
        {{ errorTime }}
      </div>

      <div class="mb-3">
        <label for="InputPrice" class="form-label">Precio por Persona (Ingrese sin puntos ni comas)</label>
        <input type="text" min="0" class="form-control" id="InputPrice" v-model="formData.price" required
          @blur="validarPrecio">
      </div>

      <div v-if="errorPrice" class="alert alert-danger" role="alert">
        {{ errorPrice }}
      </div>
      
      <div class="d-grid gap-2 pb-5">
        <button class="btn btn-dark" type="submit"
          style="background-color: #182a3f; border-radius: 20px;" @click="enviarFormulario">Enviar</button>
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
        plate: "",
        origin: "",
        destiny: "",
        flight_date: "",
        time: "",
        price: "",
      },
      errorDate: "",   // Verifica si hubo un error con la fecha
      errorPrice: "",   //Verifica si hubo un error con el precio
      errorPlate: "",   //Verifica que la placa no contenga espacios en blanco
      errorOrigin: "",  //Verifica si hubo un error con el orige
      errorDestiny: "", //Verifica si hubo un error con el destino
      errorTime: "",    //Verifica si hubo un error con la hora
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


    validarPrecio() {
      const price = this.formData.price;
      const soloDigitos = /^\d+$/; // Expresión regular para verificar que solo hay dígitos

      if (!soloDigitos.test(price)) {
        this.errorPrice = 'El precio solo puede contener numeros';
      } else {
        this.errorPrice = '';
      }
    },
    validarPlaca() {
      const placa = this.formData.plate;
      //Expresion regular para que no hayan espacios en blanco ni al inicio ni al final de la cadena
      const sinEspacios = /^(?!\s)(.*\S)(?!\s)*$/;
      if(placa && !sinEspacios.test(placa)){
        this.errorPlate = 'La placa no puede contener espacios en blanco ni al inicio ni al final.';
      } else {
        this.errorPlate = '';
      }
    },
    validarOrigen() {
      //Colocar la validacion respectiva
    },
    validarDestino() {
      //Colocar la validacion respectiva
    },
    validarFecha() {
      //Colocar la validacion respectiva
    },
    validarHora() {
      //Colocar la validacion respectiva
    },
  },
};
</script>
<template>
    <div class="container">
      <button @click="agregarTarjeta" class="btn btn-primary">Agregar</button>
  
      <div v-if="mostrarModal">
        <div class="modal-overlay" @click="cerrarModal"></div>
        <div class="modal" tabindex="-1">
          <div class="modal-content">
            <button @click="cerrarModal" class="btn btn-danger modal-close-btn">Cerrar</button>
            <p>Opciones de la tarjeta:</p>
            <button @click="editarBalance" class="btn btn-warning">Editar Balance</button>
            <button @click="eliminarTarjeta" class="btn btn-danger">Eliminar</button>
          </div>
        </div>
      </div>
  
      <div class="tarjeta-lista">
    <div v-for="(tarjeta, index) in tarjetas" :key="index" class="tarjeta" @click="mostrarOpciones(index)">
      <div class="tarjeta-info">
        <img src="visa_logo.png" alt="Visa Logo" class="tarjeta-logo" />
        <div>
          <p class="tarjeta-number">{{ formatNumeroTarjeta(tarjeta.number) }}</p>
          <p class="tarjeta-saldo">Saldo: {{ tarjeta.cash }}</p>
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
        tarjetas: [],
        mostrarModal: false,
        tarjetaSeleccionada: null,
      };
    },
    mounted() {
      this.obtenerTarjetas();
    },
    methods: {
      async obtenerTarjetas() {
        try {
          const response = await axios.get('http://127.0.0.1:8000/api/v1/user/cards', {
            headers: {
              Authorization: `Bearer ${this.$store.state.token}`,
            },
          });
          this.tarjetas = response.data.cards;
        } catch (error) {
          console.error('Error al obtener tarjetas:', error);
        }
      },
      agregarTarjeta() {
        // ir a ruta addCard
        this.$router.push('/addCard');
      },
      mostrarOpciones(index) {
        this.tarjetaSeleccionada = index;
        this.mostrarModal = true;
      },
      editarBalance() {
        // Lógica para editar el balance de la tarjeta seleccionada
      },
      eliminarTarjeta() {
        // Lógica para eliminar la tarjeta seleccionada
      },
      cerrarModal() {
        this.mostrarModal = false;
      },
      formatNumeroTarjeta(numero) {
        // Lógica para dividir el número de tarjeta en cuartetos, por ejemplo
        return numero.match(/.{1,4}/g).join(' ');
      },
    },
  };
  </script>
  
  <style scoped>
  .container {
    text-align: center;
  }
  
  .tarjeta-lista {
    margin-top: 20px;
    background-color: #5CCDA7;
    border-radius: 10px;
    padding: 10px;
    display: flex;
    flex-direction: column; /* Cambiado a columna */
    align-items: center; /* Alineado al centro */
  }
  
  .tarjeta {
  margin-bottom: 10px; /* Espaciado entre tarjetas */
  cursor: pointer;
  background-color: white;
  border: 2px solid #5CCDA7; /* Borde con color de fondo */
  border-radius: 8px; /* Bordes redondeados */
  padding: 15px; /* Espaciado interno aumentado */
  width: 90%; /* Ajustar el ancho de la tarjeta al 90% del contenedor verde */
  box-sizing: border-box; /* Considerar el borde y el relleno en el ancho total */
}
  
  .tarjeta-info {
    display: flex;
    align-items: center;
  }
  
  .tarjeta-logo {
    width: 30px;
    margin-right: 10px;
  }
  
  .tarjeta-number {
    font-size: 18px;
    font-weight: bold;
    margin: 0;
  }
  
  .tarjeta-saldo {
    margin: 0;
  }
  </style>
  
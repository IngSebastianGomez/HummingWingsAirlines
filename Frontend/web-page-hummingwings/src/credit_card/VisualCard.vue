<template>
    <div class="container">
      <button @click="agregarTarjeta" class="btn btn-primary">Agregar</button>
  
      <div v-if="mostrarModal">
        <div class="modal-overlay" @click="cerrarModal"></div>
        <div class="modal" tabindex="-1">
          <button @click="cerrarModal" class="btn btn-danger modal-close-btn">Cerrar</button>
          <p>Opciones de la tarjeta:</p>
          <button @click="editarBalance" class="btn btn-warning">Editar Balance</button>
          <button @click="eliminarTarjeta" class="btn btn-danger">Eliminar</button>
        </div>
      </div>
  
      <div class="tarjeta-lista">
        <div v-for="(tarjeta, index) in tarjetas" :key="index" @click="mostrarOpciones(index)">
          {{ tarjeta.nombre }}
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import 'bootstrap/dist/css/bootstrap.min.css';
  import 'bootstrap/dist/js/bootstrap.bundle.min.js';
  
  export default {
    data() {
      return {
        tarjetas: [
          { nombre: 'Tarjeta 1', balance: 1000 },
          { nombre: 'Tarjeta 2', balance: 2000 },
          // Agrega más tarjetas según sea necesario
        ],
        mostrarModal: false,
        tarjetaSeleccionada: null,
      };
    },
    methods: {
      agregarTarjeta() {
        // Lógica para agregar tarjeta
        // Puedes mostrar un formulario o manejar la lógica según tu aplicación
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
    flex-wrap: wrap;
    justify-content: space-around;
  }
  
  .modal-overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.5);
    z-index: 1;
  }
  
  .modal {
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    background-color: white;
    padding: 20px;
    z-index: 2;
  }
  
  .modal-close-btn {
    margin-top: 10px;
  }
  </style>
  
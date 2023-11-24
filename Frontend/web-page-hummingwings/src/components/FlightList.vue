<!-- FlightList.vue -->
<template>
    <div class="flight-list">
      <div v-if="flights.length === 0">No hay vuelos disponibles.</div>
      <div v-else>
        <div class="flight" v-for="flight in flights" :key="flight.code_flight">
          <div class="flight-container">
            <div class="flight-info">
              <div><strong>Código de vuelo:</strong> {{ flight.code_flight }}</div>
              <div><strong>Origen:</strong> {{ flight.city_start }}</div>
              <div><strong>Destino:</strong> {{ flight.city_end }}</div>
              <div><strong>Precio del boleto:</strong> {{ flight.price_of_ticket }}</div>
              <div><strong>Fecha de salida:</strong> {{ formatDateTime(flight.date_start) }}</div>
              <div><strong>Horas de vuelo:</strong> {{ flight.hours_of_flight }}</div>
            </div>
            <div class="button-container">
              <button type="button" class="btn btn-danger" @click="deleteFlight(flight.code_flight)">Eliminar</button>
              <button type="button" class="btn btn-info" @click="editFlight">Editar</button>
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
        flights: [],
        loading: true
      };
    },
    created() {
      this.fetchFlights();
    },
    methods: {
      fetchFlights() {
        // Obtener el token desde Vuex
        const token = this.$store.state.token;
  
        // Configurar la solicitud de Axios
        const axiosConfig = {
          headers: {
            Authorization: `Bearer ${token}`
          }
        };
  
        // Realizar la solicitud GET al backend
        axios.get('http://127.0.0.1:8000/api/v1/flight', axiosConfig)
          .then(response => {
            this.flights = response.data.data;
            this.loading = false;
          })
          .catch(error => {
            console.error('Error al obtener la lista de vuelos:', error);
            this.loading = false;
          });
      },
      formatDateTime(dateTime) {
    // Eliminamos el último carácter (Z) y reemplazamos la T por un espacio
    return dateTime.slice(0, -1).replace('T', ' ');
  },
      deleteFlight(codeFlight) {
        // Obtener el token desde Vuex
        const token = this.$store.state.token;
  
        // Configurar la solicitud de Axios
        const axiosConfig = {
          headers: {
            Authorization: `Bearer ${token}`
          }
        };
  
        // Realizar la solicitud DELETE al backend
        axios.delete(`http://127.0.0.1:8000/api/v1/flight/${codeFlight}`, axiosConfig)
          .then(response => {
            console.log('Vuelo eliminado con éxito:', response.data);
            // Actualizar la lista de vuelos después de eliminar
            this.fetchFlights();
          })
          .catch(error => {
            console.error('Error al eliminar el vuelo:', error);
          });
      },
      editFlight() {
        //ir a ruta de editar vuelo
        this.$router.push('/editFlight');
      },
    }
  };
  </script>
  
  <style scoped>
  .flight-list {
    margin-top: 20px;
  }
  
  .flight {
    margin-bottom: 10px;
  }
  
  .flight-container {
    background-color: #4CAF50; /* Color verde */
    border-radius: 10px;
    padding: 10px;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
  
  .flight-info {
    color: white; /* Texto blanco */
    font-size: 14px;
  }
  
  .button-container {
    display: flex;
    gap: 10px;
  }
  
  .loading-message {
    font-size: 16px;
    font-weight: bold;
  }
  </style>
  
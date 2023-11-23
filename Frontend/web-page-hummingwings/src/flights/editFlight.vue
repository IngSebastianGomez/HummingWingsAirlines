<template>
  <div class="container-sm mt-5 mb-5">
    <h1>Editar Vuelo</h1>
    <div class="form-container">
      <form @submit.prevent="submitForm">
        <div class="mb-3">
          <label for="origin" class="form-label">Origin:</label>
          <input type="text" class="form-control" id="origin" v-model="flight.origin" required>
        </div>
        <div class="mb-3">
          <label for="destination" class="form-label">Destination:</label>
          <input type="text" class="form-control" id="destination" v-model="flight.destination" required>
        </div>
        <div class="mb-3">
          <label for="departure-date" class="form-label">Departure Date:</label>
          <input type="date" class="form-control" id="departure-date" v-model="flight.departureDate" :min="currentDate" required>
        </div>
        <div class="mb-3">
          <label for="departure-time" class="form-label">Departure Time:</label>
          <input type="time" class="form-control" id="departure-time" v-model="flight.departureTime" required pattern="HH:mm">
        </div>
        <div class="mb-3">
          <label for="scheduled-flight-times" class="form-label">Scheduled Flight Times:</label>
          <input type="text" class="form-control" id="scheduled-flight-times" v-model="flight.scheduledFlightTimes" required>
        </div>
        <div class="mb-3">
          <label for="international-flight" class="form-label">International Flight:</label>
          <input type="checkbox" class="form-check-input" id="international-flight" v-model="flight.isInternational">
        </div>
        <div class="mb-3">
          <label for="flight-value" class="form-label">Flight Value:</label>
          <input type="number" class="form-control" id="flight-value" v-model="flight.value" required>
        </div>
        <button class="btn btn-primary" type="submit">Submit</button>
      </form>
    </div>
  </div>
</template>

<script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        flight: {
          origin: '',
          destination: '',
          departureDate: '',
          departureTime: '',
          scheduledFlightTimes: '',
          isInternational: false,
          value: 0
        }
      };
    },
    computed: {
      currentDate() {
        const today = new Date();
        const year = today.getFullYear();
        let month = today.getMonth() + 1;
        month = month < 10 ? '0' + month : month;
        let day = today.getDate();
        day = day < 10 ? '0' + day : day;
        return `${year}-${month}-${day}`;
      }
    },
    methods: {
      submitForm() {
        const jsonPayload = {
          city_end: this.flight.destination,
          city_start: this.flight.origin,
          date_start: `${this.formatDate(this.flight.departureDate)}-${this.flight.departureTime}`,
          hours_of_flight: 1,
          is_international: this.flight.isInternational,
          price_of_ticket: this.flight.value
        };
  
        const token = this.$store.state.token;
  
        const axiosConfig = {
          headers: {
            Authorization: `Bearer ${token}`
          }
        };
  
        axios.post('http://127.0.0.1:8000/api/v1/flight', jsonPayload, axiosConfig)
          .then(response => {
            console.log('Respuesta del servidor:', response.data);
            this.$router.push('/manageFlight');
          })
          .catch(error => {
            console.error('Error al enviar el formulario:', error);
          });
      },
      
      formatDate(date) {
        const [year, month, day] = date.split('-');
        return `${year}-${month}-${day}`;
      }
    }
  };
  </script>
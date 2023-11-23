<template>
    <div class="container">
      <div class="form-container">
        <form @submit.prevent="submitForm">
          <div class="form-group">
            <label for="origin">Origin:</label>
            <input type="text" id="origin" v-model="flight.origin" required>
          </div>
          <div class="form-group">
            <label for="destination">Destination:</label>
            <input type="text" id="destination" v-model="flight.destination" required>
          </div>
          <div class="form-group">
            <label for="departure-date">Departure Date:</label>
            <input type="date" id="departure-date" v-model="flight.departureDate" :min="currentDate" required>
          </div>
          <div class="form-group">
            <label for="departure-time">Departure Time:</label>
            <input type="time" id="departure-time" v-model="flight.departureTime" required pattern="HH:mm">
          </div>
          <div class="form-group">
            <label for="scheduled-flight-times">Scheduled Flight Times:</label>
            <input type="text" id="scheduled-flight-times" v-model="flight.scheduledFlightTimes" required>
          </div>
          <div class="form-group">
            <label for="international-flight">International Flight:</label>
            <input type="checkbox" id="international-flight" v-model="flight.isInternational">
          </div>
          <div class="form-group">
            <label for="flight-value">Flight Value:</label>
            <input type="number" id="flight-value" v-model="flight.value" required>
          </div>
          <button type="submit">Submit</button>
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
  
  <style scoped>
  .container {
    display: flex;
    align-items: center;
    justify-content: center;
    height: 100vh;
  }
  
  .form-container {
    background-color: #d2f5d2; /* Verde claro */
    border-radius: 10px;
    padding: 20px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  }
  
  .form-group {
    margin-bottom: 1rem;
  }
  
  button[type="submit"] {
    padding: 0.5rem 1rem;
    background-color: #007bff;
    color: #fff;
    border: none;
    cursor: pointer;
  }

  </style>
  

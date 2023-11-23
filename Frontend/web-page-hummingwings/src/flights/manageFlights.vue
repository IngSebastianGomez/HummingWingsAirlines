
<template>
    <div class="container">
      <div class="form-container">
        <!-- Botón para agregar vuelo -->
        <button class="btn btn-primary" @click="goToAddFlight">Add Flight</button>
  
        <!-- Lista de vuelos -->
        <flight-list></flight-list>
      </div>
    </div>
  </template>
  
  <script>
  import FlightList from '@/components/FlightList.vue'; // Ajusta la ruta según la estructura de tu proyecto
  
  export default {
    components: {
      FlightList
    },
    methods: {
      goToAddFlight() {
        this.$router.push('/AddFlight');
      }
    }
  };
  </script>
  
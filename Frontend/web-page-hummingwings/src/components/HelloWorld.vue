<template>
  <div class="container">
    <div class="hello">
      <CarouselSlider />
    </div>
    <!--Pestañas-->
    <nav>
      <div class="nav nav-tabs" id="nav-tab" role="tablist">
        <button
          class="nav-link active"
          id="nav-flights-tab"
          data-bs-toggle="tab"
          data-bs-target="#nav-flights"
          type="button"
          role="tab"
          aria-controls="nav-flights"
          aria-selected="true"
          style="background-color: #006FEE; color: black;"
        >
          Vuelos
        </button>

        <button
          class="nav-link"
          id="nav-checkin-tab"
          data-bs-toggle="tab"
          data-bs-target="#nav-checkin"
          type="button"
          role="tab"
          aria-controls="nav-checkin"
          aria-selected="false"
          style="background-color: #17C964; color: black;"
        >
          Check In
        </button>
      </div>
    </nav>

    <!--Contenido de las pestañas, solo se muestra el contenido de la pestaña activa-->
    <div class="tab-content" id="nav-tabContent">
    <!--Pestaña de vuelos-->
      <div
        class="tab-pane fade show active p-3"
        id="nav-flights"
        role="tabpanel"
        aria-labelledby="nav-flights-tab"
        style="background-color: #459CFF;"
      >
        <form class="light" @submit.prevent="searchFlights">
          <div class="row">
            <div class="col-md-6 mb-3">
              <label for="origin" class="form-label">Origen</label>
              <input
                class="form-control"
                type="search"
                id="origin"
                v-model="origin"
                aria-label="Search"
              />
            </div>
            <div class="col-md-6 mb-3">
              <label for="destination" class="form-label">Destino</label>
              <input
                class="form-control"
                type="search"
                id="destination"
                v-model="destination"
                aria-label="Search"
              />
            </div>
          </div>
          <div class="row">
            <div class="col-md-6 mb-3">
              <label for="departure-date" class="form-label">Fecha de salida</label>
              <input
                class="form-control"
                type="date"
                id="departure-date"
                v-model="departureDate"
                :min="currentDate"
                aria-label="Search"
              />
            </div>
            <div v-if="roundTrip" class="col-md-6 mb-3">
              <label for="return-date" class="form-label">Fecha de regreso</label>
              <input
                class="form-control"
                type="date"
                id="return-date"
                v-model="returnDate"
                :min="departureDate"
                aria-label="Search"
              />
            </div>
          </div>
          <!-- ... (el resto del formulario permanece igual) ... -->
          <div class="row">
            <div class="col">
              <label class="form-check-label text-white ml-2">
                <input
                  class="form-check-input"
                  type="checkbox"
                  v-model="roundTrip"
                />
                Ida y Vuelta
              </label>
            </div>
            <div class="col">
              <!--mostrar mensaje "numero de pasajeros"-->
              <label class="form-check-label text-white ml-2">
                Número de pasajeros <input
                class="form-control me-2"
                type="number"
                placeholder="Número de Pasajeros"
                v-model="passengers"
                min="1"
                aria-label="Search"
              />
              </label>
            </div>
            <div class="col">
              <button class="btn btn-primary" type="submit">Buscar</button>
            </div>
          </div>
        </form>
        <!-- Resultados de la búsqueda -->
        <div v-if="searchResults.length > 0" class="mt-4">
          <h2>Resultados de la Búsqueda</h2>
          <ul>
            <li v-for="result in searchResults" :key="result.code_flight">
              {{ result.city_start }} a {{ result.city_end }} - {{ formatDateTime(result.date_start) }}
              <p>Asientos disponibles: {{ result.sold_seats }}</p>
              <p>Precio: {{ result.price_of_ticket }}</p>
              <button @click="reserveFlight(result)" class="btn btn-success ml-2">Reservar</button>
            </li>
          </ul>
        </div>
      </div>
      <!--Pestaña de checkin-->
      <!--Agregar el v-if para que se muestre si no se esta logeado-->
      <div
        class="tab-pane fade p-3"
        id="nav-checkin"
        role="tabpanel"
        aria-labelledby="nav-checkin-tab"
        style="background-color: #489C86;"
      >
        <form class="d-flex mt-2 light">
          <input
            class="form-control me-2"
            type="search"
            placeholder="Número de identificación"
            aria-label="Search"
          />
          <input
            class="form-control me-2"
            type="search"
            placeholder="Código de reserva"
            aria-label="Search"
          />
          <button class="btn btn-primary" type="submit">Enviar</button>
        </form>
      </div>
    </div>

    <!--Para darle un espacio en la parte de abajo y no quede la parte de búsqueda pegada al suelo-->
    <div class="container">
      <div class="row">
        <div class="col">
          <p>.</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import CarouselSlider from './CarouselSliderAd.vue';
import axios from 'axios';

export default {
  name: 'HelloWorld',
  components: {
    CarouselSlider,
  },
  data() {
    return {
      origin: '',
      destination: '',
      departureDate: '',
      returnDate: '',
      roundTrip: false,
      passengers: 1,
      searchResults: [],
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
    },
  },
  methods: {
    formatDateTime(dateTime) {
      // Lógica para formatear la fecha y hora según tus necesidades
      // Por ejemplo, eliminar la 'T' y 'Z' y ajustar el formato
      return dateTime.replace('T', ' ').replace('Z', '');
    },
    searchFlights() {
      const url = 'http://127.0.0.1:8000/api/v1/search/flight';
      const travelType = this.roundTrip ? 'round_trip' : 'one_way';

      const params = {
        city_start: this.origin,
        city_end: this.destination,
        date_start: this.departureDate,
        travel_type: travelType,
        seats: this.passengers,
      };

      if (this.roundTrip) {
        params.return_date = this.returnDate;
      }

      axios.get(url, { params })
        .then(response => {
          this.searchResults = response.data.data;
        })
        .catch(error => {
          console.error('Error al buscar vuelos:', error);
        });
    },
    reserveFlight(result) {
      console.log('Vuelo reservado:', result);
      // Lógica para la reserva del vuelo, puedes redirigir a otra página, mostrar un modal, etc.
    },
  },
};
</script>

<style>
.hello {
  justify-content: center;
  align-items: center;
  min-height: 60vh;
  background-color: blueviolet;
}
</style>

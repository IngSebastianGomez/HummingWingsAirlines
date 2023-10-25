<template>
  <div class="container">
    <div class="hello">
      <CarouselSlider/>
    </div>
    <!--Pestañas-->
    <nav>
      <div class="nav nav-tabs" id="nav-tab" role="tablist">
        <button class="nav-link active" id="nav-flights-tab" data-bs-toggle="tab"
        data-bs-target="#nav-flights" type="button" role="tab" aria-controls="nav-flights"
        aria-selected="true" style="background-color: #006FEE; color: black;">Vuelos</button>

        <button class="nav-link" id="nav-checkin-tab" data-bs-toggle="tab"
        data-bs-target="#nav-checkin" type="button" role="tab" aria-controls="nav-checkin"
        aria-selected="false" style="background-color: #17C964; color: black;">Check In</button>
      </div>
    </nav>

    <!--Contenido de las pestañas, solo se muestra el contenido de la pestaña activa-->
    <div class="tab-content" id="nav-tabContent">
      <div class="tab-pane fade show active p-3" id="nav-flights" role="tabpanel"
      aria-labelledby= "nav-flights-tab" style="background-color: #459CFF;">
        <form class="d-flex mt-2 light">
          <input class="form-control me-2" type="search" placeholder="Origin" aria-label="Search">
          <input class="form-control me-2" type="search" placeholder="Departure" aria-label="Search">
          <input class="form-control me-2" type="search" placeholder="Date1" aria-label="Search">
          <input class="form-control me-2" type="search" placeholder="Date2" aria-label="Search">
          <button class="btn btn-primary" type="submit">Search</button>
        </form>
      </div>

      <div class="tab-pane fade p-3" id="nav-checkin" role="tabpanel"
      aria-labelledby= "nav-checkin-tab" style="background-color: #489C86;">
        <form class="d-flex mt-2 light">
          <input class="form-control me-2" type="search" placeholder="Number of identification" aria-label="Search">
          <input class="form-control me-2" type="search" placeholder="booking code" aria-label="Search">
          <button class="btn btn-primary" type="submit">Submit</button>
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
import CarouselSlider from './CarouselSliderAd.vue'


export default {
  name: 'HelloWorld',
  components: {
    CarouselSlider,
  }
}

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
.hello {
    justify-content: center;
    align-items: center;
    min-height: 60vh; /* Usar min-height en lugar de height */
    background-color: blueviolet; /* Cambiar el color de fondo aquí */
  }
</style>
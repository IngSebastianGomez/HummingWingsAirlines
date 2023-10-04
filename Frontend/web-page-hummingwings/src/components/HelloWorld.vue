<template>
  <div class="hello">
    <CarouselSlider/>
    <p>
      <router-link to="/detail">Detail</router-link>
    </p>
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
    min-height: 100vh; /* Usar min-height en lugar de height */
    background-color: blueviolet; /* Cambiar el color de fondo aquí */
  }
</style>
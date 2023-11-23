<template>
    <div>
      <!-- Contenido principal de la página -->
      <div class="contenido-principal">
  
        <!-- Formulario de Personalización de Reserva -->
        <div class="formulario-personalizacion">
          <h2>Personaliza tu Viaje</h2>
          <p>Selecciona los servicios adicionales que deseas incluir en tu reserva</p>
          <!-- Asientos Preferenciales VIP -->
<div class="mb-3 form-check">
  <input type="checkbox" class="form-check-input" id="vipSeats" v-model="selectedVipSeats" @change="updatePrice()"/>
  <label class="form-check-label" for="vipSeats">Asientos Preferenciales VIP {{ formatoPrecio(vipSeatsCost) }} COP</label>
</div>

<!-- Equipaje Adicional -->
<div class="mb-3 form-check">
  <input type="checkbox" class="form-check-input" id="extraLuggage" v-model="selectedExtraLuggage" @change="updatePrice()"/>
  <label class="form-check-label" for="extraLuggage">Equipaje Adicional {{ formatoPrecio(extraLuggageCost) }} COP</label>
</div>

<!-- Llevar una Mascota -->
<div class="mb-3 form-check">
  <input type="checkbox" class="form-check-input" id="pet" v-model="bringPet" @change="updatePrice()"/>
  <label class="form-check-label" for="pet">Llevar una Mascota {{ formatoPrecio(bringPetCost) }} COP</label>
</div>

<!-- Servicios de Conectividad -->
<div class="mb-3 form-check">
  <input type="checkbox" class="form-check-input" id="connectivity" v-model="connectivityService" @change="updatePrice()" />
  <label class="form-check-label" for="connectivity">Servicios de Conectividad {{ formatoPrecio(connectivityServiceCost) }} COP</label>
</div>

<div>
      <h3>Datos Actuales:</h3>
      <ul>
        <li><strong>Tiquete:</strong> {{ formatoPrecio(servicios.ticket.costo) }}</li>
        <li><strong>Asientos Preferenciales VIP:</strong> {{ formatoPrecio(servicios.vipSeats.costo) }}</li>
        <li><strong>Equipaje Adicional:</strong> {{ formatoPrecio(servicios.extraLuggage.costo) }}</li>
        <li><strong>Llevar una Mascota:</strong> {{ formatoPrecio(servicios.bringPet.costo) }}</li>
        <li><strong>Servicios de Conectividad:</strong> {{ formatoPrecio(servicios.connectivityService.costo) }}</li>
      </ul>
    </div>
  
          <button type="submit" class="btn btn-primary">Continuar</button>
        </div>
        <!-- Aquí puedes acceder al resultado del store -->
        
      </div>
      <PurchaseSummary />
    </div>
  </template>
  
  <script>
  import PurchaseSummary from '@/components/PurchaseSummary.vue';
  
  export default {
    name: 'makeReservation', // Nombre del componente
    components: {
      PurchaseSummary,
    },
    data() {
      return {
        precioOriginal: 0,
        //variable de control de los checkbox
        previousSelectedVipSeats: false,
        previousSelectedExtraLuggage: false,
        previousBringPet: false,
        previousConnectivityService: false,
        //variables de control de los checkbox
        selectedVipSeats: 0,
        selectedExtraLuggage: 0,
        bringPet: false,
        connectivityService: false,
        //porcentajes costo servicios 
        vipSeatsCostPercentage: 1, // 100%
        extraLuggageCostPercentage: 0.15, // 15%
        bringPetCostPercentage: 0.10, // 10%
        connectivityServiceCostPercentage: 0.10, // 10%
        //Precio final de la reserva
        vipSeatsCost : 0,
        extraLuggageCost : 0,
        bringPetCost : 0,
        connectivityServiceCost : 0,
        //diccionario 
        servicios: {
          ticket: {
            nombre: 'Tiquete',
            costo: 0,
          },
          vipSeats: {
            nombre: 'Asientos Preferenciales VIP',
            costo: 0,
          },
          extraLuggage: {
            nombre: 'Equipaje Adicional',
            costo: 0,
          },
          bringPet: {
            nombre: 'Llevar una Mascota',
            costo: 0,
          },
          connectivityService: {
            nombre: 'Servicios de Conectividad',
            costo: 0,
          },
        },
      };
    },
    computed: {
      resultadoBusqueda() {
        // Accede al resultado almacenado en el store
        return this.$store.state.resultadoBusqueda;
      },
    },
    created() {
    // Calcula el precioOriginal al entrar al componente
    if (this.resultadoBusqueda.price_of_ticket) {
      if (this.precioOriginal === 0) {
        // Almacena el precio original solo una vez al entrar al componente
        this.precioOriginal = parseFloat(this.resultadoBusqueda.price_of_ticket.replace(/,/g, ''));
        // definir el precio de los servicios
        this.vipSeatsCost = this.precioOriginal * this.vipSeatsCostPercentage;
        this.extraLuggageCost = this.precioOriginal * this.extraLuggageCostPercentage;
        this.bringPetCost = this.precioOriginal * this.bringPetCostPercentage;
        this.connectivityServiceCost = this.precioOriginal * this.connectivityServiceCostPercentage;
      }
    }
    //guardar en el diccionario
    this.servicios.ticket.costo = this.precioOriginal;
  },
    methods: {
    updatePrice() {
      
      // Lógica para actualizar el precio según los checkboxes seleccionados
      let totalPrice = this.resultadoBusqueda.price_of_ticket;
      //convertir a int 
      let numericPrice = parseFloat(totalPrice.replace(/,/g, '')); // Remueve las comas y convierte a número
      // Ajusta el precio según el estado de los checkboxes
      if (this.selectedVipSeats && !this.previousSelectedVipSeats) {
        numericPrice += this.vipSeatsCost;
      } else if (!this.selectedVipSeats && this.previousSelectedVipSeats) {
        numericPrice -= this.vipSeatsCost;
      }

      if (this.selectedExtraLuggage && !this.previousSelectedExtraLuggage) {
        numericPrice += this.extraLuggageCost;
      } else if (!this.selectedExtraLuggage && this.previousSelectedExtraLuggage) {
        numericPrice -= this.extraLuggageCost;
      }

      if (this.bringPet && !this.previousBringPet) {
        numericPrice += this.bringPetCost;
      } else if (!this.bringPet && this.previousBringPet) {
        numericPrice -= this.bringPetCost;
      }

      if (this.connectivityService && !this.previousConnectivityService) {
        numericPrice += this.connectivityServiceCost;
      } else if (!this.connectivityService && this.previousConnectivityService) {
        numericPrice -= this.connectivityServiceCost;
      }

      // Actualiza el valor en resultadoBusqueda
      console.log(numericPrice);
      this.$store.commit('updatePriceInResultadoBusqueda', numericPrice.toString() + '.00');
      // Actualiza los estados anteriores
      this.previousSelectedVipSeats = this.selectedVipSeats;
      this.previousSelectedExtraLuggage = this.selectedExtraLuggage;
      this.previousBringPet = this.bringPet;
      this.previousConnectivityService = this.connectivityService;

      // Actualiza los datos de los servicios
      this.servicios.vipSeats.costo = this.selectedVipSeats ? this.vipSeatsCost : 0;
      this.servicios.extraLuggage.costo = this.selectedExtraLuggage ? this.extraLuggageCost : 0;
      this.servicios.bringPet.costo = this.bringPet ? this.bringPetCost : 0;
      this.servicios.connectivityService.costo = this.connectivityService ? this.connectivityServiceCost : 0;
    },
    formatoPrecio(precio) {
        // Formatear el precio con el signo de dólar y formato de miles y millones
        const formatter = new Intl.NumberFormat('es-CO', {
          style: 'currency',
          currency: 'COP',
        });
        return formatter.format(precio);
      },
  },
  };
  </script>
  
  <style scoped>
  /* Estilos para el contenido principal */
  .contenido-principal {
    background-color: #d3f7d2; /* Color verde claro */
    border-radius: 10px; /* Esquinas redondeadas */
    padding: 20px; /* Márgenes internos */
    margin: 20px; /* Márgenes externos */
    margin-bottom: 100px;
  }
  
  /* Estilos para el formulario de personalización */
  .formulario-personalizacion {
  margin-top: 20px; /* Márgenes superiores para separar del contenido principal */
  max-height: 500px; /* Altura máxima para mostrar; ajusta según sea necesario */
  overflow-y: auto; /* Agrega scroll vertical si el contenido excede la altura máxima */
  margin-bottom: 100px;
}
  
  /* Puedes agregar estilos adicionales según sea necesario */
  </style>
  
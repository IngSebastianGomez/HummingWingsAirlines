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

<!-- segundo formulario --> 
<div class="container-sm mt-5 mb-5">
    <h1 style="color:black">Informacion de Pasajeros</h1>
    <br>
    <h2>Pasajero passenger</h2>
    <form>
      <div class="form-container">
        <div class="mb-3">
          <label for="name" class="form-label">Nombre</label>
          <input type="text" class="form-control" id="name" v-model="passName" required>
        </div>
        <div class="mb-3">
          <label for="lastName" class="form-label">Apellido</label>
          <input type="text" class="form-control" id="lastName" v-model="passLastName" required>
        </div>
        <div class="mb-3">
          <label for="identityDocument" class="form-label">Documento de identidad</label>
          <select class="form-select" v-model="passDocType" required>
            <option value="" disabled selected>Documento de identidad</option>
            <option value="C.C">C.C.</option>
            <option value="Pasaporte">Pasaporte</option>
          </select>
        </div>
        <div class="mb-3">
          <label for="name" class="form-label">Numero de documento</label>
          <input type="text" class="form-control" id="name" v-model="passDocNum" required>
        </div>
        <div class="mb-3">
          <label for="birthday" class="form-label">Fecha de Nacimiento</label>
          <input type="date" class="form-control" id="birthday" v-model="passDateBirth" min="1924-01-01"
            max="2004-10-15" required>
        </div>
        <div class="mb-3">
          <label for="gender" class="form-label">Género</label>
          <select class="form-select" v-model="passGender" required>
            <option value="" disabled selected>Género</option>
            <option value="mele">masculino</option>
            <option value="femenino">femenino</option>
            <option value="otro">Prefiero no decirlo</option>
          </select>
        </div>
        
        <div class="mb-3">
          <label for="cellphoneNumber" class="form-label">Numero de celular</label>
          <input type="text" class="form-control" id="cellphoneNumber" v-model="passCellphone" required>
        </div>
        <div class="mb-3">
          <label for="email" class="form-label">Correo Electronico</label>
          <input type="text" class="form-control" id="email" v-model="passEmail" required>
        </div>
        
        <div class="d-grid gap-2 pb-5">
          
        </div>
      </div>
    </form>
  </div>



    <button class="btn btn-primary" type="button" style="background-color: green; color: white;" data-bs-toggle="offcanvas" data-bs-target="#offcanvasRight" aria-controls="offcanvasRight">Resumen de la compra</button>

<div class="offcanvas offcanvas-end" tabindex="-1" id="offcanvasRight" aria-labelledby="offcanvasRightLabel">
  <div class="offcanvas-header">
    <h3 id="offcanvasRightLabel">Factura</h3>
    <button type="button" class="btn-close text-reset" data-bs-dismiss="offcanvas" aria-label="Close"></button>
  </div>
  <div class="offcanvas-body">
    <div>
      <ul>
        <li><strong>Tiquete:</strong> {{ formatoPrecio(servicios.ticket.costo) }}</li>
        <li><strong>Asientos Preferenciales VIP:</strong> {{ formatoPrecio(servicios.vipSeats.costo) }}</li>
        <li><strong>Equipaje Adicional:</strong> {{ formatoPrecio(servicios.extraLuggage.costo) }}</li>
        <li><strong>Llevar una Mascota:</strong> {{ formatoPrecio(servicios.bringPet.costo) }}</li>
        <li><strong>Servicios de Conectividad:</strong> {{ formatoPrecio(servicios.connectivityService.costo) }}</li>
        <li><strong>Total:</strong> {{ formatoPrecio(servicios.totalPrice.costo) }}</li>
      </ul>
    </div>
    <button type="submit" style="background-color: green; color: white;" class="btn btn-primary" @click="enviarReservaAlServidor">Continuar</button>

  </div>
</div>

          
        </div>
        <!-- Aquí puedes acceder al resultado del store -->
        
      </div>
      <PurchaseSummary />
      
    </div>
  </template>
  
  <script>
  import PurchaseSummary from '@/components/PurchaseSummary.vue';
  import axios from 'axios';
  
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
          totalPrice: {
            nombre: 'Total',
            costo: 0,
          },
        },
        //datos para enviar del formulario al servidor
        passName: 'Diego',
        passLastName: 'Bedoya',
        passDocType: 'C.C',
        passDocNum: '103213213',
        passDateBirth: '2000-01-01',
        passGender: 'mele',
        passCellphone: '3233123323',
        passEmail: 'sebax@yopmail.com',

        
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
    this.servicios.totalPrice.costo = this.precioOriginal;
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
      //total de los servicios
      this.servicios.totalPrice.costo = numericPrice;
    },
    formatoPrecio(precio) {
        // Formatear el precio con el signo de dólar y formato de miles y millones
        const formatter = new Intl.NumberFormat('es-CO', {
          style: 'currency',
          currency: 'COP',
        });
        return formatter.format(precio);
      },
      calcularEdad(fechaNacimiento) {
    // Convierte la cadena de fecha de nacimiento a un objeto de fecha
    var fechaNacimientoDate = new Date(fechaNacimiento);

    // Obtiene la fecha actual
    var fechaActual = new Date();

    // Calcula la diferencia en años
    var edad = fechaActual.getFullYear() - fechaNacimientoDate.getFullYear();

    // Verifica si aún no ha pasado el cumpleaños de este año
    if (
        fechaActual.getMonth() < fechaNacimientoDate.getMonth() ||
        (fechaActual.getMonth() === fechaNacimientoDate.getMonth() &&
            fechaActual.getDate() < fechaNacimientoDate.getDate())
    ) {
        edad--;
    }

    return edad;
}
,
      async enviarReservaAlServidor() {
      try {
        const url = 'http://127.0.0.1:8000/api/v1/booking';

        const name = this.passName;
        const LastName = this.passLastName;
        const DocType = this.passDocType;
        const DocNum = this.passDocNum;
        const DateBirth = this.passDateBirth;
        const Gender = this.passGender;
        const Cellphone = this.passCellphone;
        const Email = this.passEmail;
        const Edad = this.calcularEdad(this.passDateBirth).toString();


        
        const data = {
          flight: this.resultadoBusqueda.code_flight,
          email: 'sebax@yopmail.com',
          cellphone: Cellphone,
          status: 'en proceso',
          passengers: [
            {
              first_name: name,
              last_name: LastName,
              email: Email,
              document_type: DocType,
              document: DocNum,
              gender: Gender,
              age_range: Edad,
              birth_date: DateBirth,
              seat_code: '1A',
            },
          ],
        };

        const token = this.$store.state.token; // Asumiendo que el token está almacenado en Vuex bajo la propiedad 'token'

        const headers = {
          'Content-Type': 'application/json',
          Authorization: `Bearer ${token}`,
        };

        const response = await axios.post(url, data, { headers });

        console.log('Respuesta del servidor:', response.data);
      } catch (error) {
        console.error('Error al enviar la reserva al servidor:', error);
      }
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
    margin: 40px; /* Márgenes externos */
    margin-bottom: 100px;
  }
  
  /* Estilos para el formulario de personalización */
  .formulario-personalizacion {
  margin-top: 20px; /* Márgenes superiores para separar del contenido principal */
  margin-left: 20px; /* Márgenes izquierdos para separar del contenido principal */
  max-height: 500px; /* Altura máxima para mostrar; ajusta según sea necesario */
  overflow-y: auto; /* Agrega scroll vertical si el contenido excede la altura máxima */
  margin-bottom: 100px;
}
  
  /* Puedes agregar estilos adicionales según sea necesario */
  </style>
  
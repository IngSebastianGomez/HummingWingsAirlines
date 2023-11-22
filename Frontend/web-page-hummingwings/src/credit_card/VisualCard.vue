<template>
  <div class="container">
    <button @click="agregarTarjeta" class="btn btn-primary">Agregar</button>

    <div class="tarjeta-lista">
      <div v-for="(tarjeta, index) in tarjetas" :key="index" class="tarjeta" @click="mostrarOpciones(index)">
        <div class="tarjeta-info">
          <img :src="logoTarjeta" alt="Logo de Tarjeta" class="tarjeta-logo" />
          <div class="tarjeta-text">
            <p class="tarjeta-number">{{ formatNumeroTarjeta(tarjeta.number) }}</p>
            
          </div>
          <p class="tarjeta-saldo">Saldo: {{ tarjeta.cash }}</p>
        </div>

        <!-- Botón para mostrar/cerrar el colapso -->
        <button class="btn btn-secondary" type="button" data-bs-toggle="collapse" :data-bs-target="'#collapseExample' + index "
          aria-expanded="false" aria-controls="collapseExample" >
          Opciones
        </button>

        
        <div :id="'collapseExample' + index" class="collapse">
          <div class="card card-body">
            <p>la tarjeta seleccionada es: {{ tarjeta.id }} </p>
            <button @click="editarBalance(tarjeta.id)" class="btn btn-warning">Editar Balance</button>
            <button @click="eliminarTarjeta" class="btn btn-danger">Eliminar</button>
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
      tarjetas: [],
      mostrarModal: false,
      tarjetaSeleccionada: null,
      logoTarjeta: '', // Variable para almacenar la ruta del logo de la tarjeta
    };
  },
  mounted() {
    this.obtenerTarjetas();
  },
  methods: {
    async obtenerTarjetas() {
      try {
        const response = await axios.get('http://127.0.0.1:8000/api/v1/user/cards', {
          headers: {
            Authorization: `Bearer ${this.$store.state.token}`,
          },
        });
        this.tarjetas = response.data.cards;
      } catch (error) {
        console.error('Error al obtener tarjetas:', error);
      }
    },
    agregarTarjeta() {
      // ir a ruta addCard
      this.$router.push('/addCard');
    },
    mostrarOpciones(index) {
      this.tarjetaSeleccionada = index;
      this.mostrarModal = true;
    },
    async editarBalance(cardId) {
      const nuevoBalance = parseInt(prompt('Ingrese el nuevo balance:', 0), 10); // Puedes usar un formulario o un método más elegante

      try {
        const response = await axios.patch(`http://127.0.0.1:8000/api/v1/card/${cardId}`, {
          cash: nuevoBalance,
        }, {
          headers: {
            Authorization: `Bearer ${this.$store.state.token}`,
          },
        });

        console.log('Balance editado con éxito:', response.data);
        // Aquí puedes actualizar la lista de tarjetas si es necesario
      } catch (error) {
        console.error('Error al editar el balance:', error);
      }
    },
    eliminarTarjeta() {
      // Lógica para eliminar la tarjeta seleccionada
    },
    cerrarModal() {
      this.mostrarModal = false;
    },
    formatNumeroTarjeta(numero) {
    // Lógica para dividir el número de tarjeta en cuartetos, por ejemplo
    const numeroFormateado = numero.match(/.{1,4}/g).join(' ');

    // Determinar el tipo de tarjeta (Visa o Mastercard) según el primer dígito
    const primerDigito = parseInt(numero.charAt(0), 10);

    if (primerDigito === 4) {
      // Visa
      this.logoTarjeta = require('@/assets/visa_logo.png'); // Asigna la ruta de la imagen Visa
    } else if (primerDigito === 5) {
      // Mastercard
      this.logoTarjeta = require('@/assets/mastercard_logo.png'); // Asigna la ruta de la imagen Mastercard
    } else {
      // Otro tipo de tarjeta, manejar según tus necesidades
      this.logoTarjeta = require('@/assets/default_logo.png'); // Puedes asignar un logo predeterminado
    }

    return numeroFormateado;
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
  flex-direction: column; /* Cambiado a columna */
  align-items: center; /* Alineado al centro */
}

.tarjeta {
  margin-bottom: 10px; /* Espaciado entre tarjetas */
  cursor: pointer;
  background-color: white;
  border: 2px solid #5CCDA7; /* Borde con color de fondo */
  border-radius: 8px; /* Bordes redondeados */
  padding: 15px; /* Espaciado interno aumentado */
  width: 90%; /* Ajustar el ancho de la tarjeta al 90% del contenedor verde */
  box-sizing: border-box; /* Considerar el borde y el relleno en el ancho total */
}

.tarjeta-info {
  display: flex;
  align-items: center;
}

.tarjeta-logo {
  width: 30px;
  margin-right: 10px;
}

.tarjeta-text {
  flex: 1; /* Hace que ocupe el espacio restante */
}

.tarjeta-number {
  font-size: 18px;
  font-weight: bold;
  margin: 0;
}

.tarjeta-saldo {
  margin: 0;
}
</style>

  
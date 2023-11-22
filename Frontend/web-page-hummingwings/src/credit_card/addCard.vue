<template>
    <div class="page-container">
      <div class="form-container">
        <form @submit.prevent="submitForm">
          <div>
            <label for="cardNumber">Card Number</label>
            <input type="text" id="cardNumber" v-model="cardNumber" required>
            <span v-if="!validCardNumber">Please enter a valid card number</span>
          </div>
          <div>
            <label for="expirationDate" class="form-label">Expiration Date (MM/YY)</label>
            <input type="date" class="form-control" id="expirationDate" v-model="expirationDate" min="2024-01-01"
            max="2050-12-15" required>
            <span v-if="!validExpirationDate">Please enter a valid expiration date</span>
          </div>
          <div>
            <label for="cvv">CVV</label>
            <input type="text" id="cvv" v-model="cvv" required>
            <span v-if="!validCvv">Please enter a valid CVV</span>
          </div>
          <button type="submit" @click="enviarFormulario">Submit</button> <!-- :disabled="!formIsValid" -->
        </form>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  import { mapState } from 'vuex';

  export default {
    data() {
      return {
        cardNumber: '',
        expirationDate: '',
        cvv: ''
      }
    },
    computed: {
      ...mapState(['id']),
      validCardNumber() {
        // Implement card number validation logic here
        return true;
      },
      validExpirationDate() {
        // Implement expiration date validation logic here
        return true;
      },
      validCvv() {
        // Implement CVV validation logic here
        return true;
      },
      formIsValid() {
        return this.validCardNumber && this.validCardholderName && this.validExpirationDate && this.validCvv;
      }
    },
    methods: {
      enviarFormulario() {
        const data = {
          code_secure: this.cvv,
          date_expire: this.expirationDate,
          number: this.cardNumber,
          owner: this.id,
        };
        const config = {
        headers: {
          Authorization: `Bearer ${this.$store.state.token}`,
        },
      };
      axios.post('http://127.0.0.1:8000/api/v1/card', data, config)
      .then(response => {
        console.log(response.data);
      })
      .catch(error => {
        console.error(error);
      });
  },
      submitForm() {
        if (this.formIsValid) {
          // Handle form submission logic here
        }
      }
    }
  }
  </script>
  
  <style scoped>
    /* Estilo para el contenedor principal de la página */
    .page-container {
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
    }
  
    /* Estilo para el contenedor del formulario */
    .form-container {
      max-width: 400px;
      padding: 20px;
      border: 1px solid #ccc;
      border-radius: 5px;
      background-color: white;
    }
  
    /* Resto del estilo (etiquetas, campos de entrada, mensajes de error, botón) como en el ejemplo anterior */
    label {
      display: block;
      margin-bottom: 5px;
      font-weight: bold;
    }
  
    input {
      width: 100%;
      padding: 10px;
      margin-bottom: 15px;
      border: 1px solid #ccc;
      border-radius: 5px;
    }
  
    span {
      color: red;
      font-size: 12px;
    }
  
    button {
      background-color: #007BFF;
      color: white;
      padding: 10px 20px;
      border: none;
      border-radius: 5px;
      cursor: pointer;
    }
  
    button:disabled {
      background-color: #ccc;
      cursor: not-allowed;
    }
  </style>
  
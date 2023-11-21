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
            <label for="cardholderName">Cardholder Name</label>
            <input type="text" id="cardholderName" v-model="cardholderName" required>
            <span v-if="!validCardholderName">Please enter a valid cardholder name</span>
          </div>
          <div>
            <label for="expirationDate">Expiration Date (MM/YY)</label>
            <input type="text" id="expirationDate" v-model="expirationDate" required>
            <span v-if="!validExpirationDate">Please enter a valid expiration date</span>
          </div>
          <div>
            <label for="cvv">CVV</label>
            <input type="text" id="cvv" v-model="cvv" required>
            <span v-if="!validCvv">Please enter a valid CVV</span>
          </div>
          <button type="submit" :disabled="!formIsValid">Submit</button>
        </form>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        cardNumber: '',
        cardholderName: '',
        expirationDate: '',
        cvv: ''
      }
    },
    computed: {
      validCardNumber() {
        // Implement card number validation logic here
        return true;
      },
      validCardholderName() {
        // Implement cardholder name validation logic here
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
  
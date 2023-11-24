<template>
<div class="container-md checkin-container">
  <h1 style="color: white">Check In</h1>
  <div class="row">
    <div class="col" style="color:black;
                            display: flex;
                            justify-content: center;">
                Please enter the reservation code</div>
  </div>
  <div class="row" v-for="(item, index) in passengers" :key="index">
    <div class="col-2">
      <label :for="'item.id'"> Pasajero {{ item.id }} </label>
      <br>
      <input type="text" v-bind:id="item.id" v-model="codes[index]" required @blur="validarEspaciosBlancos">
    </div>
  </div>
  <div class="row" v-if="!errorWhiteSpaces" style="margin-top: 2rem;">
    <div class="col">
      <button class="btn btn-primary">Enviar</button>
    </div>
  </div>
  <div class="row" v-if="errorWhiteSpaces" style="margin-top: 1rem;">
    <div class="col-5">
      <div class="alert alert-danger" role="alert">
        Los codigos no pueden ser espacios en blanco
      </div>
    </div>
  </div>
  <!-- Espacio para verificar que datos se estan guardando en codes[]
  <div class="row">
    <p>
      datos del form:
    </p>
    <pre>{{ codes }}</pre>
  </div>
  -->
</div>
</template>

<style scoped>
.checkin-container{
  border-radius: 36px;
  background: linear-gradient(0deg, rgba(0, 194, 183, 0.00) 4.08%, #5CCDA7 100%);
  padding: 2rem;
  margin-top: 1rem;
  margin-bottom: 2rem;
}
.col{
  display: flex;
  align-items: center;
  justify-content: center;
}
.row{
  display: flex;
  align-items: center;
  justify-content: center;
}
label{
  color:white;
}
input[type=text]{
  width: 100%;
  height: 2rem;
  border-radius: 5px;
  border: none;
}
</style>

<script>
  export default{
    data(){
      return{
        passengers:[{id:"101", name:"Andres"},
                    {id:"102", name:"Jose"},
                    {id:"103", name:"Fabi"}],
        codes:[],
        errorWhiteSpaces: null,
      }
    },
    methods:{
      validarEspaciosBlancos() {
        const sinEspacios = /^(?!\s)(.*\S)(?!\s)*$/;
        for(var i = 0; i < this.codes.length; i++){
          const nombreAValidar = this.codes[i];
          if(nombreAValidar && !sinEspacios.test(nombreAValidar) ||
              nombreAValidar == ""){
            this.errorWhiteSpaces = true;
            break;
          } else {
            this.errorWhiteSpaces = false;
          }
        }
        
    },
    }
  }
</script>
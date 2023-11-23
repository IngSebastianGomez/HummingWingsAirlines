<template>
  <div class="container-sm mt-5 mb-5">
    <h1 style="color:black">Informacion de Pasajeros</h1>
    <br>
    <h2>Pasajero passenger.id</h2>
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
            <option value="C.C.">C.C.</option>
            <option value="Pasaporte">Pasaporte</option>
          </select>
        </div>
        <div class="mb-3">
          <label for="name" class="form-label">Numero de documento</label>
          <input type="text" class="form-control" id="name" v-model="passName" required>
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
            <option value="masculino">masculino</option>
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
          <button class="btn btn-dark"
                  type="submit"
                  style="background-color: #182a3f; border-radius: 40px;"
                  @click="enviarFormulario">Enviar</button>
        </div>
      </div>
    </form>
  </div>
</template>

<script>
  export default{
    data(){
      return{
        passName: null,
        passLastName: null,
        passDocType: null,
        passDocNum: null,
        passDateBirth: null,
        passGender: null,
        passCellphone: null,
        passEmail: null,
      }
    },
    methods:{
      enviarFormulario(){
        console.log('Editar segun la necesidad')
      }
    }
  }
</script>
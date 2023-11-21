<template>
  <div class="container">
    <!-- Button trigger modal -->
    <button type="button"
            class="btn btn-primary"
            data-bs-toggle="modal"
            data-bs-target="#exampleModal">
      Boton de eliminar
    </button>

    <!-- Modal -->
    <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header" style="background-color: red;">
            <h5 class="modal-title" id="exampleModalLabel">Aviso</h5>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            <p>¿Estas seguro de que quieres eliminar este ___ ?</p>
          </div>
          <div class="modal-footer justify-content-evenly">
            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cancelar</button>
            <button type="button" class="btn btn-primary" @click="redirigirAlInicio" data-bs-dismiss="modal">Eliminar</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  export default{
    data() {
      return{
        onOffDialog: false,
      };
    },
    methods:{
      redirigirAlInicio() {
      this.$router.push('/');
    }
    }
  }
</script>
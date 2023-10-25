<template>
  <div class="container mt-5">
    <div class="card">
      <div class="card-body" style="background-color: #489C86;">
        <h1 class="card-title" style="background-color: #019970; color: #fff; padding: 10px;">
          Lista de Cuentas de Administradores
        </h1>
        <ul class="list-group">
  <li v-for="admin in admins" :key="admin.id" class="list-group-item">
    <div class="row">
      <div class="col-md-1">
        <div class="field-title">ID:</div>
        {{ admin.id }}
      </div>
      <div class="col-md-2">
        <div class="field-title">Correo:</div>
        {{ admin.email }}
      </div>
      <div class="col-md-2">
        <div class="field-title">Nombre:</div>
        {{ admin.first_name }}
      </div>
      <div class="col-md-2">
        <div class="field-title">Apellido:</div>
        {{ admin.last_name }}
      </div>
      <div class="col-md-3">
        <div class="field-title">Estado:</div>
        {{ admin.status }}
      </div>
      <div class="col-md-2">
        <div class="d-flex justify-content-end">
          <button @click="mostrarConfirmacion(admin.id)" class="btn btn-danger" style="margin-left: 10px;">Eliminar</button>
        </div>
      </div>
    </div>
  </li>
</ul>

      </div>
    </div>

    <!-- Cuadro de diálogo de confirmación personalizado -->
    <div class="custom-modal" v-if="mostrandoConfirmacion">
      <div class="custom-modal-content">
        <div class="modal-header">
          <h5 class="modal-title">Confirmación</h5>
          <button type="button" class="btn-close" @click="cerrarConfirmacion" aria-label="Close"></button>
        </div>
        <div class="modal-body">
          ¿Estás seguro de que deseas eliminar esta cuenta de administrador?
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-secondary" @click="cerrarConfirmacion">Cancelar</button>
          <button type="button" class="btn btn-danger" @click="eliminarAdmin(adminAEliminar)">Eliminar</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import { mapState } from 'vuex';

export default {
  data() {
    return {
      admins: [],
      mostrandoConfirmacion: false,
      adminAEliminar: null,
    };
  },
  computed: {
    ...mapState(['token']),
  },
  created() {
    const token = this.token;

    if (token) {
      axios
        .get('http://127.0.0.1:8000/api/v1/user/?rol=administrador', {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        })
        .then((response) => {
          this.admins = response.data;
        })
        .catch((error) => {
          console.error('Error al obtener la lista de administradores:', error);
        });
    } else {
      console.error('Token de autorización no encontrado en el localStorage');
    }
  },
  methods: {
    mostrarConfirmacion(adminId) {
      this.adminAEliminar = adminId;
      this.mostrandoConfirmacion = true;
    },
    cerrarConfirmacion() {
      this.mostrandoConfirmacion = false;
    },
    eliminarAdmin(adminId) {
      const url = `http://127.0.0.1:8000/api/v1/user/${adminId}`;
      const data = {
        rol: 'administrador',
      };

      axios
        .delete(url, {
          headers: {
            Authorization: `Bearer ${this.token}`,
          },
          data,
        })
        .then(response => {
          this.cargarListaAdmins(); // Actualiza la lista después de eliminar

          console.log('Administrador eliminado con éxito:', response.data);
          this.cerrarConfirmacion();
        })
        .catch(error => {
          console.error('Error al eliminar administrador:', error);
        });
    },
    cargarListaAdmins() {
      axios
        .get('http://127.0.0.1:8000/api/v1/user/?rol=administrador', {
          headers: {
            Authorization: `Bearer ${this.token}`,
          },
        })
        .then(response => {
          this.admins = response.data; // Actualiza la lista de administradores
        })
        .catch(error => {
          console.error('Error al obtener la lista de administradores:', error);
        });
    },
  },
};
</script>


<style>
.custom-modal {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 9999;
}

.custom-modal-content {
  background: #fff;
  max-width: 600px;
  border-radius: 5px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
  overflow: hidden;
}
</style>
  
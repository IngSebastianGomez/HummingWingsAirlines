<template>
    <div class="resumen-compra">
      <div class="contenido-resumen">
        <!-- Aquí va tu contenido del resumen y el costo de la compra -->
        <p>Resumen de la compra</p>
        <p>Costo total: {{ formatoPrecio(resultadoBusqueda.price_of_ticket) }} COP</p>
        <div class="boton-derecha">
          <button type="button" class="btn btn-secondary btn-lg boton-resumen" disabled>Button</button>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    computed: {
      resultadoBusqueda() {
        // Accede al resultado almacenado en el store
        return this.$store.state.resultadoBusqueda;
      },
    },
    methods: {
        
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
  .resumen-compra {
    position: fixed;
    bottom: 0;
    left: 0;
    width: 100%;
    background-color: #ffffff; /* Fondo blanco o el color deseado */
    box-shadow: 0 -2px 5px rgba(0, 0, 0, 0.1);
    margin: 0;
  }
  
  .contenido-resumen {
    display: flex;
    flex-direction: column; /* Alinea los elementos en una columna */
    justify-content: space-between; /* Alinea los elementos a ambos lados del contenedor */
    align-items: flex-start; /* Alinea los elementos a la izquierda */
    padding: 10px;
    color: #000000; /* Color de texto, ajusta según sea necesario */
  }
  
  .boton-derecha {
    margin-left: auto; /* Mueve el botón hacia la derecha utilizando el auto margin */
  }
  
  .boton-resumen {
    max-width: 150px; /* Ajusta el ancho máximo del botón según tus necesidades */
    margin-top: 10px; /* Agrega un margen superior para separar el botón del texto */
  }
  </style>
    
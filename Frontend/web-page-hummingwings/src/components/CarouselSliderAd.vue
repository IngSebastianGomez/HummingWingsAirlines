<template>
    <div class="container" style="background-color: #182a3f;"> <!--Le puse el mismo color de la pagina porque no me gustó el morado que tenía-->
      <div id="carouselExampleCaptions" class="carousel slide" data-bs-ride="carousel">
        <!--Zona de funcionalidad viene del sample de bootstrap-->
        <div class="carousel-indicators">
          <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
          <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="1" aria-label="Slide 2"></button>
          <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="2" aria-label="Slide 3"></button>
        </div>
        <!--Zona de contenido-->
        <div class="carousel-inner">
          <div class="carousel-item active">
            <img src="../assets/Bogota.jpg" class="d-block w-100 " alt="banner1">
            <div class="carousel-caption d-none d-md-block">
              <h5>BOGOTA</h5>
              <p>Aprovecha! 30% de descuento.</p>
            </div>
          </div>
          <div class="carousel-item">
            <img src="../assets/Medellin.jpg" class="d-block w-100 " alt="banner2">
            <div class="carousel-caption d-none d-md-block">
              <h5>MEDELLIN</h5>
              <p>Disfruta de este descuento del 20%.</p>
            </div>
          </div>
          <div class="carousel-item">
            <img src="../assets/madrid.jpg" class="d-block w-100" alt="banner3">
            <div class="carousel-caption d-none d-md-block">
              <h5>MADRID</h5>
              <p>Ultimos tiquetes con el 25% de descuento!.</p>
            </div>
          </div>
        </div>
        <!--Zona de botones laterales. Viene del sample de bootstrap-->
        <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide="prev">
          <span class="carousel-control-prev-icon" aria-hidden="true"></span>
          <span class="visually-hidden">Previous</span>
        </button>
        <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide="next">
          <span class="carousel-control-next-icon" aria-hidden="true"></span>
          <span class="visually-hidden">Next</span>
        </button>
      </div>
    </div>
</template>

<style>
  .carousel-item{
    align-items: center;
  }
</style>
<template>
  <div class="container-sm mt-5 mb-5">
    <div class="row">
      <div class="col">
        <div class="container-flex p-3" style="background-color: gray; border-radius: 8px;">
          <h1>Filtrar por:</h1>
          
          
            <form class="d-flex mt-2 light">
              <label for="TopPrice" class="form-label m-2">Precio Tope</label>
              <input class="form-control me-1" id = "TopPrice" type="search" placeholder="Precio tope" aria-label="Search">
              <label for="BottTime" class="form-label m-2">Hora salida</label>
              <input class="form-control me-1" id = "BottTime" type="search" placeholder="Hora de salida" aria-label="Search">
              <button class="btn btn-primary" type="submit">Submit</button>
            </form>
          
        </div>
      </div>
    </div>
    <div class="row">
      <div class="col">
        <div class="row align-items-center">
          <div class="col">
            <h3>Departure Time</h3>
          </div>
          <div class="col">
            <h3>Arrive time</h3>
          </div>
          <div class="col">
            <h3>Price</h3>
          </div>
        </div>
        <div class="d-grid align-items-center p-2">
          <button type="button" class="btn btn-light btn-large">
            <div class="row">
              <div class="col">
                <div class="row">fechaD</div>
                <div class="row">HoraD</div>
              </div>
              <div class="col">
                <div class="row">fechaA</div>
                <div class="row">HoraA</div>
              </div>
              <div class="col">
                Price
              </div>
            </div>
          </button>
        </div>
      </div>
    </div>
  </div>
</template>
<template>
  <div class="row">
    <div class="col-7">
      <div class="plane">
        <div class="cockpit">
          <h1>Avion Nacional</h1>
        </div>
        <ol class="cabin fuselage">
          <li class="row row--1" v-for="num in 17" :key="num" >
            <ol class="seats" type="A">
              <li class="seat">
                <button type="checkbox" v-bind:id="num + 'A'"  @click="addSeat(num+'A')">
                  {{num}}A
                </button>
                
              </li>
              <li class="seat">
                <button type="checkbox" v-bind:id="num + 'B'"  @click="addSeat(num+'B')">
                  {{num}}B
                </button>
                
              </li>
              <li class="seat">
                <button type="checkbox" v-bind:id="num + 'C'"  @click="addSeat(num+'C')">
                  {{num}}C
                </button>
                
              </li>
              <li class="seat">
                <button type="checkbox" v-bind:id="num + 'D'"  @click="addSeat(num+'D')">
                  {{num}}D
                </button>
                
              </li>
              <li class="seat">
                <button type="checkbox" v-bind:id="num + 'E'"  @click="addSeat(num+'E')">
                  {{num}}E
                </button>
                
              </li>
              <li class="seat">
                <button type="checkbox" v-bind:id="num + 'F'"  @click="addSeat(num+'F')">
                  {{num}}F
                </button>
                
              </li>
            </ol>
          </li>
        </ol>
      </div>
    </div>
    <div class="col-4">
      <div class="container mb-3">
        <h1 style="color: white;">Pasajeros</h1>
        <ul>
          <li class="list-group-item" v-for="item in passengers" :key="item.id">
            <div class="btn myButton" @click="addCurrentPassenger(item.id)">
                <div class="row">
                  <div class="col">
                    {{ item.name }}
                  </div>
                </div>
                <div class="row">
                  <div class="col">
                    {{ item.id }}
                  </div>
                </div>
            </div>
          </li>
        </ul>
        <button class="btn btn-primary">Enviar</button>
        <div v-if="errorSeatOcuppied" class="alert alert-danger" role="alert">
          Los asientos seleccionados estan ocupados.
        </div>

      </div>
      <div style="background-color: #489C86; border-radius: 1rem; padding-left: 1rem;">
        <p>Info de asientos seleccionados</p>
        <div class="row" v-for="element in selectedSeat" :key="element.passenger">
          <hr>
          <p>Pasajero: {{ element.passenger }}</p>
          <p>Asiento seleccionado: {{ element.idSeat }}</p>
          
          <br>
        </div>
    </div>
    </div>
  </div>
</template>

<style scoped>
*,*:before,*:after {
  box-sizing: border-box;
}
html {
  font-size: 16px;
}
.plane {
  margin: 20px auto;
  max-width: 350px;
}
.cockpit {
  height: 250px; 
  position: relative;
  overflow: hidden;
  text-align: center;
  border-bottom: 5px solid #d8d8d8;
  &:before {
    content: "";
    display: block;
    position: absolute;
    top: 0;
    left: 0;
    height: 500px;
    width: 100%;
    border-radius: 50%;
    border-right: 5px solid #d8d8d8;
    border-left: 5px solid #d8d8d8;
  }
  h1 {
    width: 60%;
    margin: 100px auto 35px auto;
    color: white;
  }

}
.fuselage {
  border-right: 5px solid #d8d8d8;
  border-left: 5px solid #d8d8d8;
}
ol {
  list-style: none;
  padding: 0;
  margin: 0;
}
.seats {
  display: flex;
  flex-direction: row;
  flex-wrap: nowrap;
  justify-content: flex-start;  
}

.seat {
  display: flex;
  flex: 0 0 14%;
  padding: 5px;
  position: relative;  
  &:nth-child(3) {
    margin-right: 14%;
  }

}
.myButton {
  background-color: #489C86;
  border-radius: 5px;
  display: block;
  margin: 8px;
  
  &:hover {
    cursor: pointer;
    box-shadow: 0 0 0px 2px #5C6AFF;
  }

  &:focus {
    color: #bada55;
  }
}

@-webkit-keyframes rubberBand {
  0% {
    -webkit-transform: scale3d(1, 1, 1);
            transform: scale3d(1, 1, 1);
  }

  30% {
    -webkit-transform: scale3d(1.25, 0.75, 1);
            transform: scale3d(1.25, 0.75, 1);
  }

  40% {
    -webkit-transform: scale3d(0.75, 1.25, 1);
            transform: scale3d(0.75, 1.25, 1);
  }

  50% {
    -webkit-transform: scale3d(1.15, 0.85, 1);
            transform: scale3d(1.15, 0.85, 1);
  }

  65% {
    -webkit-transform: scale3d(.95, 1.05, 1);
            transform: scale3d(.95, 1.05, 1);
  }

  75% {
    -webkit-transform: scale3d(1.05, .95, 1);
            transform: scale3d(1.05, .95, 1);
  }

  100% {
    -webkit-transform: scale3d(1, 1, 1);
            transform: scale3d(1, 1, 1);
  }
}

@keyframes rubberBand {
  0% {
    -webkit-transform: scale3d(1, 1, 1);
            transform: scale3d(1, 1, 1);
  }

  30% {
    -webkit-transform: scale3d(1.25, 0.75, 1);
            transform: scale3d(1.25, 0.75, 1);
  }

  40% {
    -webkit-transform: scale3d(0.75, 1.25, 1);
            transform: scale3d(0.75, 1.25, 1);
  }

  50% {
    -webkit-transform: scale3d(1.15, 0.85, 1);
            transform: scale3d(1.15, 0.85, 1);
  }

  65% {
    -webkit-transform: scale3d(.95, 1.05, 1);
            transform: scale3d(.95, 1.05, 1);
  }

  75% {
    -webkit-transform: scale3d(1.05, .95, 1);
            transform: scale3d(1.05, .95, 1);
  }

  100% {
    -webkit-transform: scale3d(1, 1, 1);
            transform: scale3d(1, 1, 1);
  }
}
.rubberBand {
  -webkit-animation-name: rubberBand;
          animation-name: rubberBand;
}
</style>

<script>
  export default{
    data(){
      return{
        occupied: ['1A', '2B', '3C', '4D', '5E', '6F'],
        passengers: [ {id:"101", name:"Andres"},
                      {id:"102", name:"Jose"},
                      {id:"103", name:"Fabi"}],
        currentPassenger: '',
        selectedSeat: [],
        another: [],
        errorSeatOcuppied: false,
      };
    },
    methods:{
      addSeat(currentSeat){
        const cp = this.currentPassenger;
        const seatPassenger = {idSeat: currentSeat, passenger: cp};
        var existPair = false;

        if(this.occupied.includes(currentSeat)){
          this.errorSeatOcuppied = true;
        }
        else if(this.selectedSeat.length == 0){
          this.selectedSeat.push(seatPassenger);
          this.errorSeatOcuppied = false;
        }
        else{
          this.errorSeatOcuppied = false;
          this.selectedSeat.forEach(function(element){
            if(element.passenger === cp){
              element.idSeat = currentSeat;
              existPair = true;
            }
          });
          if(!existPair && this.selectedSeat.length < this.passengers.length){
            this.selectedSeat.push(seatPassenger);
          }
        }
      },
      addCurrentPassenger(idItem){
        this.currentPassenger = idItem;
      }
    }
  }
</script>
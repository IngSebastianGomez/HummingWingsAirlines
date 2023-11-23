<template>
  <div class="row">
    <div class="col-7">
      <div class="plane">
        <div class="cockpit">
          <h1>Avion Nacional</h1>
        </div>
        <ol class="cabin fuselage">
          <li class="row row--1" v-for="num in 10" :key="num" >
            <ol class="seats" type="A">
              <li class="seat">
                <input type="checkbox" v-bind:id="num + 'A'" v-model="currentSeat" @click="addSeat"/>
                <label for="1A">{{num}}A</label>
              </li>
              <li class="seat">
                <input type="checkbox" v-bind:id="num + 'B'" />
                <label for="1B">{{num}}B</label>
              </li>
              <li class="seat">
                <input type="checkbox" v-bind:id="num + 'C'" />
                <label for="1C">{{num}}C</label>
              </li>
              <li class="seat">
                <input type="checkbox" v-bind:id="num + 'D'" />
                <label for="1D">{{num}}D</label>
              </li>
              <li class="seat">
                <input type="checkbox" v-bind:id="num + 'E'" />
                <label for="1E">{{num}}E</label>
              </li>
              <li class="seat">
                <input type="checkbox" v-bind:id="num + 'F'" />
                <label for="1F">{{num}}F</label>
              </li>
            </ol>
          </li>
          <!--
          <li class="row row--2">
            <ol class="seats" type="A">
              <li class="seat">
                <input type="checkbox" :disabled="validate == '2A'" id="2A" />
                <label for="2A">2A</label>
              </li>
              <li class="seat">
                <input type="checkbox" :disabled="validate == '2B'" id="2B" />
                <label for="2B">2B</label>
              </li>
              <li class="seat">
                <input type="checkbox" :disabled="validate == '2C'" id="2C" />
                <label for="2C">2C</label>
              </li>
              <li class="seat">
                <input type="checkbox" :disabled="validate == '2D'" id="2D" />
                <label for="2D">2D</label>
              </li>
              <li class="seat">
                <input type="checkbox" :disabled="validate == '2E'" id="2E" />
                <label for="2E">2E</label>
              </li>
              <li class="seat">
                <input type="checkbox" :disabled="validate == '2F'" id="2F" />
                <label for="2F">2F</label>
              </li>
            </ol>
          </li>
          <li class="row row--3">
            <ol class="seats" type="A">
              <li class="seat">
                <input type="checkbox" :disabled="validate == '3A'" id="3A" />
                <label for="3A">3A</label>
              </li>
              <li class="seat">
                <input type="checkbox" :disabled="validate == '3B'" id="3B" />
                <label for="3B">3B</label>
              </li>
              <li class="seat">
                <input type="checkbox" :disabled="validate == '3C'" id="3C" />
                <label for="3C">3C</label>
              </li>
              <li class="seat">
                <input type="checkbox" :disabled="validate == '3D'" id="3D" />
                <label for="3D">3D</label>
              </li>
              <li class="seat">
                <input type="checkbox" :disabled="validate == '3E'" id="3E" />
                <label for="3E">3E</label>
              </li>
              <li class="seat">
                <input type="checkbox" :disabled="validate == '3F'" id="3F" />
                <label for="3F">3F</label>
              </li>
            </ol>
          </li>
          <li class="row row--4">
            <ol class="seats" type="A">
              <li class="seat">
                <input type="checkbox" :disabled="validate == '4A'" id="4A" />
                <label for="4A">4A</label>
              </li>
              <li class="seat">
                <input type="checkbox" :disabled="validate == '4B'" id="4B" />
                <label for="4B">4B</label>
              </li>
              <li class="seat">
                <input type="checkbox" :disabled="validate == '4C'" id="4C" />
                <label for="4C">4C</label>
              </li>
              <li class="seat">
                <input type="checkbox" :disabled="validate == '4D'" id="4D" />
                <label for="4D">4D</label>
              </li>
              <li class="seat">
                <input type="checkbox" :disabled="validate == '4E'" id="4E" />
                <label for="4E">4E</label>
              </li>
              <li class="seat">
                <input type="checkbox" :disabled="validate == '4F'" id="4F" />
                <label for="4F">4F</label>
              </li>
            </ol>
          </li>
          <li class="row row--5">
            <ol class="seats" type="A">
              <li class="seat">
                <input type="checkbox" :disabled="validate == '5A'" id="5A" />
                <label for="5A">5A</label>
              </li>
              <li class="seat">
                <input type="checkbox" :disabled="validate == '5B'" id="5B" />
                <label for="5B">5B</label>
              </li>
              <li class="seat">
                <input type="checkbox" :disabled="validate == '5C'" id="5C" />
                <label for="5C">5C</label>
              </li>
              <li class="seat">
                <input type="checkbox" :disabled="validate == '5D'" id="5D" />
                <label for="5D">5D</label>
              </li>
              <li class="seat">
                <input type="checkbox" :disabled="validate == '5E'" id="5E" />
                <label for="5E">5E</label>
              </li>
              <li class="seat">
                <input type="checkbox" :disabled="validate == '5F'" id="5F" />
                <label for="5F">5F</label>
              </li>
            </ol>
          </li>
          <li class="row row--6">
            <ol class="seats" type="A">
              <li class="seat">
                <input type="checkbox" :disabled="validate == '6A'" id="6A" />
                <label for="6A">6A</label>
              </li>
              <li class="seat">
                <input type="checkbox" :disabled="validate == '6B'" id="6B" />
                <label for="6B">6B</label>
              </li>
              <li class="seat">
                <input type="checkbox" :disabled="validate == '6C'" id="6C" />
                <label for="6C">6C</label>
              </li>
              <li class="seat">
                <input type="checkbox" :disabled="validate == '6D'" id="6D" />
                <label for="6D">6D</label>
              </li>
              <li class="seat">
                <input type="checkbox" :disabled="validate == '6E'" id="6E" />
                <label for="6E">6E</label>
              </li>
              <li class="seat">
                <input type="checkbox" :disabled="validate == '6F'" id="6F" />
                <label for="6F">6F</label>
              </li>
            </ol>
          </li>
          <li class="row row--7">
            <ol class="seats" type="A">
              <li class="seat">
                <input type="checkbox" :disabled="validate == '7A'" id="7A" />
                <label for="7A">7A</label>
              </li>
              <li class="seat">
                <input type="checkbox" :disabled="validate == '7B'" id="7B" />
                <label for="7B">7B</label>
              </li>
              <li class="seat">
                <input type="checkbox" :disabled="validate == '7C'" id="7C" />
                <label for="7C">7C</label>
              </li>
              <li class="seat">
                <input type="checkbox" :disabled="validate == '7D'" id="7D" />
                <label for="7D">7D</label>
              </li>
              <li class="seat">
                <input type="checkbox" :disabled="validate == '7E'" id="7E" />
                <label for="7E">7E</label>
              </li>
              <li class="seat">
                <input type="checkbox" :disabled="validate == '7F'" id="7F" />
                <label for="7F">7F</label>
              </li>
            </ol>
          </li>
          <li class="row row--8">
            <ol class="seats" type="A">
              <li class="seat">
                <input type="checkbox" :disabled="validate == '8A'" id="8A" />
                <label for="8A">8A</label>
              </li>
              <li class="seat">
                <input type="checkbox" :disabled="validate == '8B'" id="8B" />
                <label for="8B">8B</label>
              </li>
              <li class="seat">
                <input type="checkbox" :disabled="validate == '8C'" id="8C" />
                <label for="8C">8C</label>
              </li>
              <li class="seat">
                <input type="checkbox" :disabled="validate == '8D'" id="8D" />
                <label for="8D">8D</label>
              </li>
              <li class="seat">
                <input type="checkbox" :disabled="validate == '8E'" id="8E" />
                <label for="8E">8E</label>
              </li>
              <li class="seat">
                <input type="checkbox" :disabled="validate == '8F'" id="8F" />
                <label for="8F">8F</label>
              </li>
            </ol>
          </li>
          <li class="row row--9">
            <ol class="seats" type="A">
              <li class="seat">
                <input type="checkbox" :disabled="validate == '9A'" id="9A" />
                <label for="9A">9A</label>
              </li>
              <li class="seat">
                <input type="checkbox" :disabled="validate == '9B'" id="9B" />
                <label for="9B">9B</label>
              </li>
              <li class="seat">
                <input type="checkbox" :disabled="validate == '9C'" id="9C" />
                <label for="9C">9C</label>
              </li>
              <li class="seat">
                <input type="checkbox" :disabled="validate == '9D'" id="9D" />
                <label for="9D">9D</label>
              </li>
              <li class="seat">
                <input type="checkbox" :disabled="validate == '9E'" id="9E" />
                <label for="9E">9E</label>
              </li>
              <li class="seat">
                <input type="checkbox" :disabled="validate == '9F'" id="9F" />
                <label for="9F">9F</label>
              </li>
            </ol>
          </li>
          <li class="row row--10">
            <ol class="seats" type="A">
              <li class="seat">
                <input type="checkbox" :disabled="validate == '10A'" id="10A" />
                <label for="10A">10A</label>
              </li>
              <li class="seat">
                <input type="checkbox" :disabled="validate == '10B'" id="10B" />
                <label for="10B">10B</label>
              </li>
              <li class="seat">
                <input type="checkbox" :disabled="validate == '10C'" id="10C" />
                <label for="10C">10C</label>
              </li>
              <li class="seat">
                <input type="checkbox" :disabled="validate == '10D'" id="10D" />
                <label for="10D">10D</label>
              </li>
              <li class="seat">
                <input type="checkbox" :disabled="validate == '10E'" id="10E" />
                <label for="10E">10E</label>
              </li>
              <li class="seat">
                <input type="checkbox" :disabled="validate == '10F'" id="10F" />
                <label for="10F">10F</label>
              </li>
            </ol>
          </li>
          -->
        </ol>
      </div>
    </div>
    <div class="col-4">
      <div class="container mb-3">
        <h1 style="color: white;">Pasajeros</h1>
        <ul>
          <li class="list-group-item" v-for="item in passengers" :key="item.id">
            <div class="btn myButton" @click="currentPassenger = item.id">
              <label for="">
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
              </label>
            </div>
          </li>
        </ul>
        <button class="btn btn-primary">Enviar</button>
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
  input[type=checkbox] {
    position: absolute;
    opacity: 0;
  }
  input[type=checkbox]:checked {
    + label {
      background: #bada55;      
      -webkit-animation-name: rubberBand;
          animation-name: rubberBand;
      animation-duration: 300ms;
      animation-fill-mode: both;
    }
  }
  input[type=checkbox]:disabled {
    + label {
      background: #dddddd;
      text-indent: -9999px;
      overflow: hidden;
      &:after {
        content: "X";
        text-indent: 0;
        position: absolute;
        top: 4px;
        left: 50%;
        transform: translate(-50%, 0%);
      }
      &:hover {
        box-shadow: none;
        cursor: not-allowed;
      }
    }
  }
  label {    
    display: block;
    position: relative;    
    width: 100%;    
    text-align: center;
    font-size: 14px;
    font-weight: bold;
    line-height: 1.5rem;
    padding: 4px 0;
    background: #F42536;
    border-radius: 5px;
    animation-duration: 300ms;
    animation-fill-mode: both;
    
    &:hover {
      cursor: pointer;
      box-shadow: 0 0 0px 2px #5C6AFF;
    }
    
  }
}
.myButton {
  background-color: #489C86;
  border-radius: 5px;
  display: block;
  margin: 1rem;
  
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
        valid: ['1A', '2B', '3C', '4D', '5E', '6F'],
        passengers: [ {id:"101", name:"Andres"},
                      {id:"102", name:"Jose"},
                      {id:"103", name:"Fabi"}],
        currentPassenger: '',
        currentSeat:'',
        selectedSeat: [],

      };
    },
    methods:{
      addSeat(){
        const seatPassenger = {idSeat: this.currentSeat, passenger: this.currentPassenger};
        if(this.selectedSeat.length == 0){
          this.selectedSeat.push(seatPassenger);
          console.log(this.selectedSeat.id, this.selectedSeat.passenger);
        }
        else if(this.selectedSeat.length <= this.passengers.length){
          this.selectedSeat.forEach(function(element){
            if(element.passenger === this.currentPassenger){
              element.id = this.currentSeat;
            }
            console.log(this.selectedSeat.id, this.selectedSeat.passenger);
          });
        }
      },
    }
  }
</script>
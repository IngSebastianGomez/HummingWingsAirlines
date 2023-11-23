//LIBRERIAS
import { createApp } from 'vue'
import App from './App.vue'
import {createRouter, createWebHashHistory} from 'vue-router';
import "bootstrap/dist/css/bootstrap.min.css"
import "bootstrap"
<<<<<<< HEAD
import "bootstrap/dist/js/bootstrap.bundle"
=======

//RUTAS DE COMPONENTES 
>>>>>>> origin/integracion
import HelloWorld from './components/HelloWorld.vue'
import DetailComponent from './components/DetailComponent.vue'
import LoginRoot from './views/LoginRoot.vue'
import OpcionesRoot from './views/OpcionesRoot.vue'
import storage from '../storage'
import CreateAdmin from './views/CreateAdmin.vue'
import RegistroUsuario from './components/RegistroUsuario.vue'
import ListaAdministradores from './views/ListaAdministradores.vue'
import LoginUser from './views/LoginUser.vue'
import AdminOptions from './views/AdminOptions.vue'
import VisualDatos from './views/VisualDatos.vue'
import ConfirmAdmin from './emails/ConfirmAdmin.vue'
import ConfirmUser from './emails/ConfirmUser.vue'
<<<<<<< HEAD
import TestingVuetify from './views/WarningWindow.vue'
import AddFlight from './views/AddFlight.vue'
import Results from './views/SearchResults.vue'
import AirplaneSeat from './views/AirplaneSeatMap.vue'
=======
import addCard from './credit_card/addCard.vue'
import listCard from './credit_card/listCard.vue'
import VisualCard from './credit_card/VisualCard.vue'
import AddFlight from './flights/AddFlight.vue'
import manageFlight from './flights/manageFlights.vue'
>>>>>>> origin/integracion

const About = { template: '<div>About</div>' }

//definir rutas
const routes = [
  { path: '/', component: HelloWorld }, 
  { path: '/about', component: About },
  { path: '/loginRoot', component: LoginRoot },
  { path: '/opcionesRoot', component: OpcionesRoot },
  { path: '/detail', component: DetailComponent},
  { path: '/CreateAdmin', component: CreateAdmin},
  { path: '/RegistroUsuario', component: RegistroUsuario},
  { path: '/ListaAdministradores', component: ListaAdministradores},
  { path: '/LoginUser', component: LoginUser},
  { path: '/AdminOptions', component: AdminOptions},
  { path: '/VisualDatos', component: VisualDatos},
  { path: '/addCard', component: addCard},
  { path: '/listCard', component: listCard},
  { path: '/VisualCard', component: VisualCard},
  { path: '/AddFlight', component: AddFlight},
  { path: '/manageFlight', component: manageFlight},
  {
    path: '/ConfirmarAdmin/:pk/:token',
    name: 'ConfirmarAdmin',
    component: ConfirmAdmin, // Reemplaza con el componente que corresponda
  },
  {
    path: '/ConfirmarUser/:pk/:token',
    name: 'ConfirmarUser',
    component: ConfirmUser, // Reemplaza con el componente que corresponda
  },
  { path: '/TestVuetify', component: TestingVuetify},
  { path: '/AddFlight', component: AddFlight},
  { path: '/Results', component: Results },
  { path: '/AirplaneSeatMap', component: AirplaneSeat},
  
]
//crear obejto rutas de vue router
const router = createRouter({
  history: createWebHashHistory(),
  routes,
});

//instancia de vue
export default router;

//Vue.use(BootstrapVue)
const app = createApp(App)
app.use(router)
app.use(storage); // Agregar Vuex a la aplicación
app.mount('#app');

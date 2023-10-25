import { createApp } from 'vue'
import App from './App.vue'
import {createRouter, createWebHashHistory} from 'vue-router';
import "bootstrap/dist/css/bootstrap.min.css"
import "bootstrap"
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

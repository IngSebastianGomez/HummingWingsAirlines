import { createApp } from 'vue'
import App from './App.vue'
import {createRouter, createWebHashHistory} from 'vue-router';
import "bootstrap/dist/css/bootstrap.min.css"
import "bootstrap"
import HelloWorld from './components/HelloWorld.vue'
import DetailComponent from './components/DetailComponent.vue'
import LoginRoot from './views/LoginRoot.vue'

const About = { template: '<div>About</div>' }

//definir rutas
const routes = [
  { path: '/', component: HelloWorld },
  { path: '/about', component: About },
  { path: '/login', component: LoginRoot },
  { path: '/hello', component: HelloWorld },
  { path: '/detail', component: DetailComponent}
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

app.mount('#app');

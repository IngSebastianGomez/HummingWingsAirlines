import { createStore } from 'vuex';

const storage = createStore({
  state: {
    id: null,
    username: 'pepito sin iniciar sesion',
    type: '',
    loggedIn: false,
  },
  mutations: {
    setId(state, id) {
      state.id = id;
    },
    setUsername(state, username) {
      state.username = username;
    },
    setType(state, type) {
      state.type = type;
    },
    loginLogged(state) {
      state.loggedIn = true;
    },
    logoutLogged(state) {
      state.loggedIn = false;
    },
  },
  actions: {
    logout({ commit }) {
      // Restablece las propiedades a sus valores iniciales
      commit('setUsername', 'pepito sin iniciar');
      commit('setId', null);
      commit('setType', null);
      commit('logoutLogged',false);
      // Elimina el token del Local Storage
      localStorage.removeItem('sessionToken');
    },
  },
});

export default storage;


import { createStore } from 'vuex';
import VuexPersistence from 'vuex-persist';
const storage = createStore({
  state: {
    id: null,
    username: 'pepito sin iniciar sesion',
    type: '',
    loggedIn: false,
    token: null,  // Agrega el campo token
    refresh: null,  // Agrega el campo refresh
    email: '',  // Agrega el campo email
    cellphone: '',  // Agrega el campo cellphone
    first_name: '',  // Agrega el campo first_name
    last_name: '',  // Agrega el campo last_name
    gender: '',  // Agrega el campo gender
    rol: '',  // Agrega el campo rol
    status: '',  // Agrega el campo status
    document: '',  // Agrega el campo document
    document_type: '',  // Agrega el campo document_type
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
    // Agrega las mutaciones para actualizar los campos token y refresh
    setToken(state, token) {
      state.token = token;
    },
    setRefresh(state, refresh) {
      state.refresh = refresh;
    },
    setEmail(state, email) {
      state.email = email;
    },
    setCellphone(state, cellphone) {
      state.cellphone = cellphone;
    },
    setFirstName(state, first_name) {
      state.first_name = first_name;
    },
    setLastName(state, last_name) {
      state.last_name = last_name;
    },
    setGender(state, gender) {
      state.gender = gender;
    },
    setRol(state, rol) {
      state.rol = rol;
    },
    setStatus(state, status) {
      state.status = status;
    },
    setDocument(state, document) {
      state.document = document;
    },
    setDocumentType(state, document_type) {
      state.document_type = document_type;
    },
  },
  actions: {
    logout({ commit }) {
      const initialState = {
        id: null,
        username: 'pepito sin iniciar sesion',
        type: '',
        loggedIn: false,
        token: null,
        refresh: null,
        email: '',
        cellphone: '',
        first_name: '',
        last_name: '',
        gender: '',
        rol: '',
        status: '',
        document: '',
        document_type: '',
      };

      commit('setUsername', initialState.username);
      commit('setId', initialState.id);
      commit('setType', initialState.type);
      commit('logoutLogged', initialState.loggedIn);
      commit('setToken', initialState.token);
      commit('setRefresh', initialState.refresh);
      commit('setEmail', initialState.email);
      commit('setCellphone', initialState.cellphone);
      commit('setFirstName', initialState.first_name);
      commit('setLastName', initialState.last_name);
      commit('setGender', initialState.gender);
      commit('setRol', initialState.rol);
      commit('setStatus', initialState.status);
      commit('setDocument', initialState.document);
      commit('setDocumentType', initialState.document_type);

      // Elimina el token del Local Storage
      localStorage.removeItem('sessionToken');
    },
  },
  plugins: [
    new VuexPersistence({
      storage: window.localStorage,
    }).plugin,
  ],
});

export default storage;


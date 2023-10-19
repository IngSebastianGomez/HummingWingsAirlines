import { createStore } from 'vuex';

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
      // Restablece las propiedades a sus valores iniciales
      commit('setUsername', 'pepito sin iniciar');
      commit('setId', null);
      commit('setType', null);
      commit('logoutLogged',false);
      commit('setToken', null);
      commit('setRefresh', null);
      commit('setEmail', '');
      commit('setCellphone', '');
      commit('setFirstName', '');
      commit('setLastName', '');
      commit('setGender', '');
      commit('setRol', '');
      commit('setStatus', '');
      commit('setDocument', '');  
      commit('setDocumentType', '');
      // Elimina el token del Local Storage
      localStorage.removeItem('sessionToken');
    },
  },
});

export default storage;


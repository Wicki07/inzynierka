import Vue from 'vue'
import Vuex from 'vuex'
import configuration from "./modules/configuration"
import user from "./modules/user"

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    test: false,

  },
  getters: {

  },
  mutations: {


  },
  actions: {
  },
  modules: {
    configuration,
    user
  }
})

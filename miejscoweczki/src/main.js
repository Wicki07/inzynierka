import Vue from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify'
import router from './router'
import store from './store'
import VueGeolocation from 'vue-browser-geolocation'
import * as VueGoogleMaps from 'vue2-google-maps'


Vue.config.productionTip = false

Vue.use(VueGeolocation)
Vue.use(VueGoogleMaps, {
  load: {
    key: 'AIzaSyBlJWXtuf4qEtips8retdT1_MdTbFi9dL0'
  },
  installComponents: false
})

new Vue({
  vuetify,
  router,
  store,
  render: h => h(App)
}).$mount('#app')

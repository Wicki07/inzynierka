import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import vuetify from "./plugins/vuetify";
import 'leaflet/dist/leaflet.css';
import '../node_modules/leaflet-geosearch/dist/geosearch.css';

import postsModule from "./modules/posts";
import authenticationModule from "./modules/authentication";

import { registerModules } from "./register-modules";

registerModules({
  posts: postsModule,
  authentication: authenticationModule,
});

Vue.config.productionTip = false;

new Vue({
  router,
  store,
  vuetify,
  render: (h) => h(App),
}).$mount("#app");

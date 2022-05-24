import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import vuetify from "./plugins/vuetify";
import 'leaflet/dist/leaflet.css';
import '../node_modules/leaflet-geosearch/dist/geosearch.css';
import "@mdi/font/css/materialdesignicons.css";

import postsModule from "./modules/posts";
import authenticationModule from "./modules/authentication";
import userPanelModule from "./modules/userPanel";

import { registerModules } from "./register-modules";

registerModules({
  posts: postsModule,
  authentication: authenticationModule,
  userPanel: userPanelModule,
});

Vue.config.productionTip = false;

new Vue({
  router,
  store,
  vuetify,
  render: (h) => h(App),
}).$mount("#app");

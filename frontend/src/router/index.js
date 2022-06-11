import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";



Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home
  }
];

const router = new VueRouter({
  // mode: "history",
  base: process.env.VUE_APP_BASE_URL432,
  routes,
});

export default router;

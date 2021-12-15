import Vue from 'vue'
import VueRouter from 'vue-router'

import Register from '../components/authentication/Register.vue'
import Login from '../components/authentication/Login.vue'
import Activate from '../components/authentication/Activate.vue'

Vue.use(VueRouter)

const routes = [

  {
    path: '/login',
    name: 'Login',
    component: Login
  },



  {
    path: '/register',
    name: 'Register',
    component: Register,
  },
  {
    path: '/activate/:code',
    name: 'Activate',
    component: Activate,
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router

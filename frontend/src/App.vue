<template>
  <v-app dark>
    <mainheader></mainheader>
    <v-main>
      <v-container fluid>

      <!-- If using vue-router -->
      <router-view></router-view>
    </v-container>
    </v-main>
    <mainfooter></mainfooter>
  </v-app>
</template>

<script>
import mainfooter from './views/Mainfoot';
import mainheader from './views/Mainhead';
import {axiosAPI} from './axiosAPI';
import { mapActions } from "vuex"

export default {
  name: 'App',

  components: {
    mainfooter,
    mainheader,
  },

  data: () => ({
    
    
  }),
  methods: {
    ...mapActions(["setUser"])
  },
  created(){
    // sprawdzenie czy refresh token istnieje
    console.log(localStorage.getItem('token'))
    if(localStorage.getItem('token')){
      axiosAPI.get('/api/auth/user').then(res => {
        this.setUser(res.data)
      }).catch(err =>{err})
    }
    else{
      return
    }
  },
};
</script>

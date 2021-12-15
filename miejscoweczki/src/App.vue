<template>
  <v-app dark>
    <mainheader></mainheader>
    <v-main style="padding:64px 0 32px;position:fixed;bottom:0;top:0;width:100%">
      <router-view></router-view>
    </v-main>
    <mainfooter></mainfooter>
  </v-app>
</template>

<script>
import mainfooter from './components/layout/Mainfoot';
import mainheader from './components/layout/Mainhead';
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
      })
    }
    else{
      return
    }
  },
};
</script>

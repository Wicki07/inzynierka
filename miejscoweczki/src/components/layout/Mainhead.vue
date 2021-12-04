<template>
  <v-app-bar  app flat dark class="navy">
    <v-row>
      <v-btn 
        text :to="'/login'"
      >
        Zaloguj
      </v-btn>
      <v-btn 
        text :to="'/register'"
      >
        Rejestracja
      </v-btn>
      <v-btn text >Opcje</v-btn>
    </v-row>
  </v-app-bar>
</template>
<script>
// import { mapState, mapGetters, mapMutations } from "vuex";
export default {
    
  data(){
    return {

    }
  },
  computed: {
  },

  methods: {

  }
}
</script>

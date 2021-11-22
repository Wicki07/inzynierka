<template>
  <v-app-bar  app flat dark class="navy">
    <v-row>
      <v-btn 
        text
      >
        Zaloguj
      </v-btn>
      <v-btn 
        text :to="'/logout'"
      >
        Wyloguj
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

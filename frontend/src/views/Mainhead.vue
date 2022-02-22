<template>
  <v-app-bar app flat dark class="blue">
    <v-row>
      <v-btn v-if="!isAuthenticated" text :to="'/login'"> Zaloguj </v-btn>
      <v-btn v-if="!isAuthenticated" text :to="'/register'">
        Rejestracja
      </v-btn>
      <v-btn v-if="isAuthenticated" text @click="logout">Wyloguj</v-btn>
      <p v-if="isAuthenticated">Witaj {{ user }}</p>
    </v-row>
  </v-app-bar>
</template>
<script>
import { mapState, mapActions } from "vuex";
import { axiosAPI } from "../axiosAPI";
export default {
  data() {
    return {};
  },
  computed: {
    ...mapState({
      isAuthenticated: (state) => state.user.isAuthenticated,
      user: (state) => state.user.username,
    }),
  },

  methods: {
    ...mapActions(["resetUser"]),
    logout() {
      axiosAPI
        .post("http://127.0.0.1:8000/api/auth/logout")
        .then(() => {
          this.resetUser();
        })
        .catch();
    },
  },
};
</script>

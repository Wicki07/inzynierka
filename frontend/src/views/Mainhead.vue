<template>
  <v-app-bar
    app
    flat
    style="box-shadow: 0 1rem 3rem rgba(0, 0, 0, 0.175) !important; height: 75px; z-index: 9999;"
    class="white px-16"
  >
    <v-row class="d-flex align-center mx-auto" style="max-width: 1160px;">
      <v-col class="pt-5">
        <v-img
          class="logo"
          height="75"
          width="100"
          :aspect-ratio="1"
          src="@/assets/logo.jpg"
          @click="home"
        ></v-img>
      </v-col>
      <v-spacer></v-spacer>
      <v-btn v-if="!isAuthenticated" text :to="'/auth/login'" color="customPrimary" class="text-subtitle-1 font-weight-medium"> Zaloguj </v-btn>
      <v-btn v-if="!isAuthenticated" text :to="'/auth/register'" color="customPrimary" class="text-subtitle-1 font-weight-medium">
        Rejestracja
      </v-btn>
      <v-btn v-if="isAuthenticated" text :to="'/auth/login'" color="customPrimary" class="text-subtitle-1 font-weight-medium"> {{user}} </v-btn>
      <v-btn v-if="isAuthenticated" text @click="logout" color="customPrimary" class="text-subtitle-1 font-weight-medium">Wyloguj</v-btn>
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
    home() {
      this.$router.push("/")
    },
  },
};
</script>
<style lang="css" scoped>
.logo :hover {
  cursor: pointer;
}
</style>
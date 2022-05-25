<template>
  <v-app>
    <mainheader></mainheader>
    <v-main>
      <v-container fluid class="pa-0">
        <v-window v-if="$route.path === '/'">
          <v-window-item>
            <v-card class="nav-bg" color="grey" height="400">
              <v-row class="fill-height" align="center" justify="center">
                <div
                  class="text-no-wrap title-row d-flex justify-center"
                  style="width: 64rem;"
                >
                  <h1 style="font-size: 5rem; font-family: 'Poppins', sans-serif;" >
                    Miejsca w pytkę
                  </h1>
                </div>
              </v-row>
            </v-card>
          </v-window-item>
        </v-window>
        <router-view class="mx-auto" style="max-width: 1160px"></router-view>
      </v-container>
    </v-main>
    <mainfooter></mainfooter>
  </v-app>
</template>

<script>
import mainfooter from "./views/Mainfoot";
import mainheader from "./views/Mainhead";
import { axiosAPI } from "./axiosAPI";
import { mapActions } from "vuex";

export default {
  name: "App",

  components: {
    mainfooter,
    mainheader,
  },

  data: () => ({}),
  methods: {
    ...mapActions(["setUser"]),
  },
  created() {
    // sprawdzenie czy refresh token istnieje
    if (localStorage.getItem("token")) {
      axiosAPI
        .get("/api/auth/user")
        .then((res) => {
          this.setUser(res.data);
        })
        .catch((err) => {
          err;
        });
    } else {
      return;
    }
  },
};
</script>
</script>
<style lang="css" scoped>
.nav-bg {
  background-image: url("./assets/bg.jpg");
  background-position: center;
  background-size: cover;
}
.title-row {
  background-color: rgba(255,255,255,0.6);
  padding: 1.5rem;
}
</style>
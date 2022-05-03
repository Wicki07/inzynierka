<template>
  <v-container>
    <p class="text-h4 my-5">Zaloguj się</p>
    <v-row class="mt-5 align-center py-5">
      <v-col>
        <v-text-field
          class="mt-5"
          v-model="username"
          label="Nazwa użytkownika"
        ></v-text-field>
        <v-text-field
          class="mt-5"
          v-model="password"
          label="Hasło"
          type="password"
          @keydown.enter="login()"
        ></v-text-field>
        <v-btn color="primary" @click="login">Zaloguj </v-btn>
      </v-col>
      <v-divider
        class="primary lighten-3 rounded-lg"
        style="border-width: 2px"
        vertical
      ></v-divider>
      <v-col class="d-flex fill-height flex-column align-center justify-center">
        <p class="text-h6 my-5 text-center">Nie masz konta?</p>
        <v-btn color="primary" @click="$router.push('/auth/register')">Zarejestruj się</v-btn>
      </v-col>
    </v-row>
    <v-card> </v-card>
  </v-container>
</template>
<script>
import axios from "axios";
import { mapActions } from "vuex";
export default {
  data() {
    return {
      username: "",
      password: "",
    };
  },
  methods: {
    ...mapActions(["setUser", "resetUser"]),
    login() {
      axios
        .post("http://127.0.0.1:8000/api/auth/login", {
          username: this.username,
          password: this.password,
        })
        .then((res) => {
          localStorage.setItem("token", res.data.token);
          this.setUser(res.data.user);
          this.$router.push({
            path: "/",
          });
        })
        .catch((err) => {
          console.log("err");
          console.log(err);
        });
    },
  },
};
</script>
<style scoped></style>

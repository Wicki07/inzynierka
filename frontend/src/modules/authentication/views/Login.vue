<template>
  <v-container>
    <v-alert
      v-model="alert"
      type="error"
      dismissible
      style="position: absolute; top: 16px; z-index: 4"
      transition="slide-x-transition"
      >Coś poszło nie tak! Spróbuj ponownie.</v-alert
    >
    <p class="text-h4 my-5">Zaloguj się</p>
    <v-row class="mt-5 align-center py-5">
      <v-col>
        <v-form ref="form" v-model="valid">
          <v-text-field
            class="mt-5"
            v-model="username"
            label="Nazwa użytkownika"
            :rules="[rules.required, rules.lengthCheck]"
          ></v-text-field>
          <v-text-field
            class="mt-5"
            v-model="password"
            label="Hasło"
            type="password"
            :rules="[rules.required]"
            @keydown.enter="login()"
          ></v-text-field>
        </v-form>
        <v-btn color="primary" @click="login">Zaloguj </v-btn>
      </v-col>
      <v-divider
        class="primary lighten-3 rounded-lg"
        style="border-width: 2px"
        vertical
      ></v-divider>
      <v-col class="d-flex fill-height flex-column align-center justify-center">
        <p class="text-h6 my-5 text-center">Nie masz konta?</p>
        <v-btn color="primary" @click="$router.push('/auth/register')"
          >Zarejestruj się</v-btn
        >
      </v-col>
    </v-row>
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
      valid: false,
      alert: false,
      rules: {
        lengthCheck: (value) =>
          (value && value.length >= 3) || "Minimalna ilość znaków to 3.",
        required: (value) => !!value || "Pole wymagane.",
      },
    };
  },
  methods: {
    ...mapActions(["setUser", "resetUser"]),
    login() {
      this.$refs.form.validate();
      if (this.valid) {
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
          .catch(() => {
            this.alert = true;
            setTimeout(() => {
              this.alert = false;
            }, 5000);
          });
      }
    },
  },
};
</script>
<style scoped></style>

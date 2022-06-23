<template>
  <v-container>
    <v-alert
      v-model="alert"
      :type="alertType"
      dismissible
      style="position: absolute; top: 16px; z-index: 4"
      transition="slide-x-transition"
      >{{ alertMsg }}</v-alert
    >
    <p class="text-h4 my-5">Zarejestruj się</p>
    <v-row class="mt-5 align-center py-5">
      <v-col cols="6">
        <v-form ref="form" v-model="valid">
          <v-text-field
            class="mt-5"
            v-model="username"
            label="Nazwa użytkownika"
            :rules="[rules.required, rules.lengthCheck]"
          ></v-text-field>
          <v-text-field
            class="mt-5"
            v-model="email"
            label="E-mail"
            :rules="[rules.required, rules.emailCheck]"
          ></v-text-field>
          <v-text-field
            class="mt-5"
            v-model="password"
            label="Hasło"
            type="password"
            :rules="[
              rules.required,
              rules.passwordLengthCheck,
              rules.passwordCheck,
            ]"
          ></v-text-field>
          <v-text-field
            class="mt-5"
            v-model="password2"
            label="Powtórz hasło"
            type="password"
            :rules="[
              rules.required,
              rules.passwordLengthCheck,
              rules.passwordCheck,
              rules.secondPasswordCheck,
            ]"
          ></v-text-field>
          <v-btn color="primary" @click="register">Zarejestruj </v-btn>
        </v-form>
      </v-col>
    </v-row>
    <v-dialog v-model="dialog" persistent max-width="400">

      <v-card>
        <v-card-title class="text-h5">
          Pomyślnie zarejestrowno
        </v-card-title>
        <v-card-text
          >Na podany mail został wysłany link do aktywacji konta. Konto nieaktywowane zostanie usunięte po 24h.</v-card-text
        >
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="primary" text @click="confirmDialog">
            Zatwierdź
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-container>
</template>
<script>
import axios from "axios";
import { mapActions } from "vuex";
import { axiosAPI } from "../../../axiosAPI";
export default {
  data() {
    return {
      username: "",
      email: "",
      password: "",
      password2: "",
      valid: false,
      dialog: false,
      alert: false,
      alertMsg: "Coś poszło nie tak! Spróbuj ponownie.",
      alertType: "error",
      rules: {
        lengthCheck: (value) =>
          (value && value.length >= 3) || "Minimalna ilość znaków to 3.",
        passwordLengthCheck: (value) =>
          (value && value.length >= 8) ||
          "Hasło powinno zawierać minimum 8 znaków.",
        emailCheck: (value) =>
          /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(value) ||
          "Nie podabo poprawnego adresu email.",
        passwordCheck: (value) =>
          /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$/.test(value) ||
          "Hasło powinno zawierać co najmniej jedną cyfrę, dużą i małą literę.",
        secondPasswordCheck: (value) =>
          value === this.password || "Podane hasła się nie zgadzają.",
        required: (value) => !!value || "Pole wymagane",
      },
    };
  },
  methods: {
    ...mapActions(["setUser"]),
    async register() {
      this.$refs.form.validate();
      if (this.valid) {
        await axiosAPI
          .post("/api/auth/register", {
            username: this.username,
            email: this.email,
            password: this.password,
          })
          .then((res) => {
            localStorage.setItem("token", res.data.token);
            this.setUser(res.data.user);
            this.dialog = true
          })
          .catch((error) => {
            this.alertMsg = error.response.data.username[0];
            this.alertType = "error";
            this.alert = true;
            setTimeout(() => {
              this.alert = false;
            }, 5000);
          });
      }
    },
    confirmDialog() {
      this.dialog = false
      window.location.replace(process.env.VUE_APP_BASE_URL);
    }
  },
};
</script>
<style scoped></style>

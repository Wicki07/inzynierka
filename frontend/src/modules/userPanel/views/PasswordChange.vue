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
    <v-btn class="mt-5" color="primary" text @click="() => $router.go(-1)">      
      <v-icon left>
        mdi-chevron-left
      </v-icon>
      Wróć
    </v-btn>
    <p class="text-h4 my-5">Zmień hasło</p>
    <v-row class="mt-5 align-center py-5">
      <v-col cols="6">
        <v-form ref="form" v-model="valid">
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
          <v-btn color="primary" @click="register">Zatwierdź </v-btn>
        </v-form>
      </v-col>
    </v-row>
  </v-container>
</template>
<script>
import { axiosAPI } from "@/axiosAPI";
import { mapActions, mapState } from "vuex";
export default {
  data() {
    return {
      password: "",
      password2: "",
      valid: false,
      alert: false,
      alertMsg: "Coś poszło nie tak! Spróbuj ponownie.",
      alertType: "error",
      rules: {
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
  computed: {
    ...mapState({
      username: (state) => state.user.username,
    }),
  },
  created() {
    window.scrollTo(0,0);
  },
  methods: {
    ...mapActions(["setUser"]),
    register() {
      this.$refs.form.validate();
      if (this.valid) {
        axiosAPI
          .post("http://127.0.0.1:8000/api/auth/passwordchange", {
            username: this.username,
            password: this.password,
          })
          .then(() => {
            this.alertMsg = "Pomyślnie zmieniono hasło";
            this.alert = true;
            this.alertType = "success";
            setTimeout(() => {
              this.alert = false;
              this.$router.go(-1)
            }, 5000);
          })
          .catch(() => {
            this.alertMsg = "Coś poszło nie tak! Spróbuj ponownie.";
            this.alert = true;
            this.alertType = "error";
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

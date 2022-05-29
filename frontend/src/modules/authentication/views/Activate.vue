<template>
  <v-container>
    <p class="text-h4 my-5">{{ this.title }}</p>
    <v-btn
      text
      color="customPrimary"
      class="text-caption font-weight-medium"
      @click="() => $router.push('/')"
    >
      Przejdź na stronę główną
    </v-btn>
  </v-container>
</template>
<script>
import { axiosAPI } from "../../../axiosAPI";
export default {
  data() {
    return {
      title: "",
    }
  },
  methods: {},
  created() {
    axiosAPI
      .get(`/api/auth/users-activation/?code=${this.$route.params.code}`)
      .then((res) => {
        this.title = "Twoje konto zostało aktywowane";
      })
      .catch((err) => {
        this.title = "Coś poszło nie tak. Spróbuj ponowanie.";
      });
  },
};
</script>
<style scoped></style>

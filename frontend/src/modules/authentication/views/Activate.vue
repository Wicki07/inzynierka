<template>
  <v-container>
    <v-card> aktywacja konta </v-card>
  </v-container>
</template>
<script>
import { axiosAPI } from "../../../axiosAPI";
export default {
  data() {},
  methods: {},
  created() {
    axiosAPI
      .get(`/api/auth/users-activation/?code=${this.$route.params.code}`)
      .then((res) => {
        console.log(res);
      })
      .catch((err) => {
        console.log(err);
      });
  },
};
</script>
<style scoped></style>

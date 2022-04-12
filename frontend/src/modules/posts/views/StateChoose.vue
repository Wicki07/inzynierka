<template>
  <div>
    <v-card height="200vh" class="ma-5 pa-5">
      <v-card-title>Wybierz województwo</v-card-title>
      <v-row>
        <v-col
          v-for="(state, index) of states"
          :key="index"
          cols="12"
          lg="3"
          sm="6"
        >
          <v-card class="mx-auto">
            <v-img
              src="https://cdn.vuetifyjs.com/images/cards/sunshine.jpg"
              height="200px"
            ></v-img>
            <v-card-title class="mb-0 pb-0">Województwo</v-card-title>
            <v-card-title class="mt-0 pt-0">{{ capitalizeFirstLetter(state) }}</v-card-title>
            <v-card-subtitle> x miejsc </v-card-subtitle>
            <v-card-actions>
              <v-btn color="orange lighten-2" text :to="`list/${state}`"> Wybierz </v-btn>
              <v-spacer></v-spacer>
              <v-btn icon>
                <v-icon>mdi-chevron-right</v-icon>
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-col>
      </v-row>
    </v-card>
  </div>
</template>
<script>
import { axiosAPI } from "@/axiosAPI";
import LocalizationSelect from "../components/LocalizationSelect.vue";
export default {
  components: {
    LocalizationSelect,
  },
  data() {
    return {
      states: [
        "dolnośląskie",
        "kujawsko-pomorskie",
        "łódzkie",
        "lubeskie",
        "lubuskie",
        "małopolskie",
        "mazowieckie",
        "opolskie",
        "podkarpackie",
        "podlaskie",
        "pomorskie",
        "śląskie",
        "świętokrzyskie",
        "warmińsko-mazurskie",
        "wielkopolskie",
        "zachodniopomorskie",
      ],
    };
  },
  methods: {
    capitalizeFirstLetter(string) {
      return string[0].toUpperCase() + string.slice(1);
    },
  },
};
</script>
<style scoped></style>

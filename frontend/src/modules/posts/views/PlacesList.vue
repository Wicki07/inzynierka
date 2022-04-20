<template>
  <div>
    <v-card class="ma-5 pa-5 rounded">
      <v-card-title v-if="state"
        >Województwo {{ capitalizeFirstLetter(state) }}</v-card-title
      >
      <v-row class="mt-3 mb-3" v-for="place of places" :key="place.id">
        <v-card class="mx-auto">
          <v-row>
            <v-col cols="3">
              <v-img
                class="rounded rounded-r-0"
                src="https://cdn.vuetifyjs.com/images/cards/sunshine.jpg"
                height="200px"
              ></v-img>
            </v-col>
            <v-col cols="9" style="height: 200px">
              <v-card-title class="mb-0 pb-0">{{ place.title }}</v-card-title>
              <v-card-subtitle>{{ place.category }}</v-card-subtitle>
              <v-card-text>
                <v-icon>mdi-map-marker-radius</v-icon>{{ place.city }}
                <v-rating
                  empty-icon="mdi-star-outline"
                  full-icon="mdi-star"
                  half-icon="mdi-star-half-full"
                  color="yellow darken-3"
                  background-color="grey darken-1"
                  hover
                  half-increments
                  length="5"
                  :value="3.5"
                ></v-rating>
              </v-card-text>
              <v-card-actions>
                <v-btn color="orange lighten-2" text @click="() => {$router.push({ name: 'place', params: { place: place, title: place.title.replace(/\s/g, '-') } })}">
                  Wybierz
                </v-btn>
                <v-spacer></v-spacer>
                <v-btn icon>
                  <v-icon>mdi-chevron-right</v-icon>
                </v-btn>
              </v-card-actions>
            </v-col>
          </v-row>
        </v-card>
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
  props: {
    state: {
      type: String,
      default() {
        return null;
      },
    },
  },
  data() {
    return {
      places: [],
    };
  },
  async created() {
    await axiosAPI.get(`/api/places/?state=${this.state}`).then((res) => {
      this.places = res.data;
    });
  },
  methods: {
    capitalizeFirstLetter(string) {
      return string[0].toUpperCase() + string.slice(1);
    },
    calcCrow(_lat1, lon1, _lat2, lon2) {
      const R = 6371; // km
      const dLat = toRad(_lat2 - _lat1);
      const dLon = toRad(lon2 - lon1);
      const lat1 = toRad(_lat1);
      const lat2 = toRad(_lat2);

      const a =
        Math.sin(dLat / 2) * Math.sin(dLat / 2) +
        Math.sin(dLon / 2) *
          Math.sin(dLon / 2) *
          Math.cos(lat1) *
          Math.cos(lat2);
      const c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));
      return R * c;
    },

    // Converts numeric degrees to radians
    toRad(Value) {
      return (Value * Math.PI) / 180;
    },
  },
};
</script>
<style scoped></style>

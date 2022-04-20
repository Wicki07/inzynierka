<template>
  <div>
    <v-card v-if="place" class="ma-5 pa-5 rounded">
      <v-card-title>{{ place.title }}</v-card-title>
      <v-card-subtitle>{{ place.category }}</v-card-subtitle>
      <v-card-subtitle>{{
        new Date(place.created_at).toISOString().slice(0, 10)
      }}</v-card-subtitle>
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
      <v-col class="justify-center" cols="12">
        <p class="d-flex text-h3 justify-center">Opis miejsca</p>
        <p class="text-body-1">{{ place.description }}</p>
      </v-col>
      <v-divider></v-divider>
      <v-col class="justify-center" cols="12">
        <p class="d-flex text-h3 justify-center">Koordynaty</p>
        <p class="d-flex text-body-1 justify-center">
          <v-icon>mdi-map-marker-radius</v-icon>{{ place.localization }}
        </p>
        <p class="d-flex text-body-1 justify-center">
          Adres: {{ addressHandle() }}
        </p>
      </v-col>
      <v-divider></v-divider>
      <v-col class="justify-center" cols="12">
        <p class="d-flex text-h3 justify-center">Zdjęcia</p>
        <v-carousel v-if="attachments.length">
          <v-carousel-item
            v-for="(item, i) in attachments"
            :key="i"
            :src="item.image"
            reverse-transition="fade-transition"
            transition="fade-transition"
          ></v-carousel-item>
        </v-carousel>
        <v-img v-else class="mx-auto" src="@/assets/default.jpg"
        width="250px"
        :aspect-ratio="16/9"
        ></v-img>
      </v-col>
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
    title: {
      type: String,
      default() {
        return null;
      },
    },
    place: {
      type: Object,
      default() {
        return null;
      },
    },
  },
  data() {
    return {
      attachments: [],
    };
  },
  async created() {
    if(this.place) {
      await axiosAPI.get(`/api/attachments/?post=${this.place.id}`).then((res) => {
        this.attachments = res.data;
      });
    }
  },
  methods: {
    addressHandle() {
      var string = "";
      if (this.place.street && this.place.street !== "undefined") {
        string += this.place.street;
      }
      if (this.place.city && this.place.city !== "undefined") {
        string += `, ${this.place.city}`;
      }
      if (this.place.post_code && this.place.post_code !== "undefined") {
        string += ` ${this.place.post_code}`;
      }
      return string;
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

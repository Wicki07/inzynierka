<template>
  <div>
    <v-card v-if="placeLocal" class="ma-5 pa-5 rounded">
      <v-card-title>{{ placeLocal.title }}</v-card-title>
      <v-card-subtitle>{{ placeLocal.category }}</v-card-subtitle>
      <v-card-subtitle>{{
        new Date(placeLocal.created_at).toISOString().slice(0, 10)
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
        <p class="text-body-1">{{ placeLocal.description }}</p>
      </v-col>
      <v-divider></v-divider>
      <v-col class="justify-center" cols="12">
        <p class="d-flex text-h3 justify-center">Koordynaty</p>
        <p class="d-flex text-body-1 justify-center">
          <v-icon>mdi-map-marker-radius</v-icon>{{ placeLocal.localization }}
        </p>
        <p class="d-flex text-body-1 justify-center">
          Adres: {{ addressHandle() }}
        </p>
      </v-col>
      <v-divider></v-divider>
      <v-col class="justify-center" cols="12">
        <p class="d-flex text-h3 justify-center">Zdjęcia</p>
        <v-carousel height="auto" v-if="attachments.length">
          <v-carousel-item
            v-for="(item, i) in attachments"
            :key="i"
            :src="item.image"
            reverse-transition="fade-transition"
            transition="fade-transition"
          ></v-carousel-item>
        </v-carousel>
        <v-img
          v-else
          class="mx-auto"
          src="@/assets/default.jpg"
          width="250px"
          :aspect-ratio="16 / 9"
        ></v-img>
      </v-col>
      <v-divider></v-divider>
      <v-col class="justify-center" cols="12">
        <comments :place="placeLocal.id"></comments>
      </v-col>
    </v-card>
  </div>
</template>
<script>
import { axiosAPI } from "@/axiosAPI";
import Comments from "../components/Comments.vue";
export default {
  components: {
    Comments,
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
      placeLocal: {},
    };
  },
  async created() {
    if (this.place) {
      this.placeLocal = this.place
      await axiosAPI
        .get(`/api/attachments/?post=${this.place.id}`)
        .then((res) => {
          this.attachments = res.data;
        });
    } else {
      await axiosAPI.get(`/api/post?id=${this.title.split("-").pop()}`).then((res) => {
        this.placeLocal = res.data
        axiosAPI
        .get(`/api/attachments/?post=${res.data.id}`)
        .then((res) => {
          this.attachments = res.data;
        });
        })
    }
  },
  methods: {
    addressHandle() {
      var string = "";
      if (this.placeLocal.street && this.placeLocal.street !== "undefined") {
        string += this.placeLocal.street;
      }
      if (this.placeLocal.city && this.placeLocal.city !== "undefined") {
        string += `, ${this.placeLocal.city}`;
      }
      if (this.placeLocal.post_code && this.placeLocal.post_code !== "undefined") {
        string += ` ${this.placeLocal.post_code}`;
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

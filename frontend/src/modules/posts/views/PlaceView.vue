<template>
  <div class="mt-16">
    <v-carousel cycle height="500px" v-if="attachments.length">
      <v-carousel-item
        v-for="(item, i) in attachments"
        :key="i"
        reverse-transition="fade-transition"
        transition="fade-transition"
      >
        <v-img
          class="mx-auto"
          :src="item.image"
          max-height="500px"
          :aspect-ratio="1"
          contain
        ></v-img>
      </v-carousel-item>
    </v-carousel>
    <v-img
      v-else
      class="mx-auto"
      src="@/assets/default.jpg"
      width="250px"
      :aspect-ratio="16 / 9"
    ></v-img>
    <v-chip small class="mt-5 white--text" color="grey darken-3" label>
      {{ placeLocal.category }}
    </v-chip>
    <v-row>
      <v-col>
        <v-card-title class="text-h4">{{ placeLocal.title }}</v-card-title>
        <v-card-subtitle>{{
          new Date(placeLocal.created_at).toISOString().slice(0, 10)
        }}</v-card-subtitle>
      </v-col>
      <v-col class="d-flex justify-end">
        <v-rating
          readonly
          empty-icon="mdi-star-outline"
          full-icon="mdi-star"
          half-icon="mdi-star-half-full"
          color="yellow darken-3"
          background-color="grey darken-1"
          hover
          half-increments
          length="5"
          :value="placeLocal.ratings"
          medium
        ></v-rating>
        <p class="mt-2 grey--text">({{ placeLocal.ratings_amount }})</p>
      </v-col>
    </v-row>
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
      <comments :place="placeLocal.id"></comments>
    </v-col>
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
    window.scrollTo(0,0);
    if (this.place) {
      this.placeLocal = this.place;
      await axiosAPI
        .get(`/api/attachments/?post=${this.place.id}`)
        .then((res) => {
          this.attachments = res.data;
        });
    } else {
      await axiosAPI
        .get(`/api/postretive?id=${this.title.split("-").pop()}`)
        .then((res) => {
          this.placeLocal = res.data[0];
          axiosAPI
            .get(`/api/attachments/?post=${res.data[0].id}`)
            .then((res) => {
              this.attachments = res.data;
            });
        });
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
      if (
        this.placeLocal.post_code &&
        this.placeLocal.post_code !== "undefined"
      ) {
        string += ` ${this.placeLocal.post_code}`;
      }
      return string;
    },
  },
};
</script>
<style scoped></style>

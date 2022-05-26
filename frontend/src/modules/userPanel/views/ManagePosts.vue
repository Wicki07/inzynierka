<template>
  <div class="pt-5">
    <v-btn class="mt-5" color="primary" text @click="() => $router.go(-1)">
      <v-icon left> mdi-chevron-left </v-icon>
      Wróć
    </v-btn>
    <v-card-title class="text-h4">Twoje posty</v-card-title>
    <div v-if="places.length !== 0">
      <v-row class="mt-3 mb-3" v-for="place of places" :key="place.id">
        <v-card
          class="mx-auto"
          @click="
            () => {
              $router.push({
                name: 'place',
                params: {
                  place: place,
                  title: place.title.replace(/\s/g, '-') + `-${place.id}`,
                },
              });
            }
          "
        >
          <v-row>
            <v-col cols="0" md="4">
              <v-img
                class="rounded rounded-r-0"
                src="https://cdn.vuetifyjs.com/images/cards/sunshine.jpg"
                height="200px"
              ></v-img>
            </v-col>
            <v-col cols="7">
              <v-card-title class="mb-0">{{ place.title }}</v-card-title>
              <v-card-subtitle class="text-caption"
                ><v-icon small>mdi-map-marker-radius</v-icon
                >{{ place.city }}</v-card-subtitle
              >
              <v-card-text>
                {{
                  place.description.lenght > 200
                    ? `${place.description.slice(0, 200)}...`
                    : place.description
                }},
                <v-row class="mt-3">
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
                    :value="place.ratings"
                    small
                  ></v-rating>
                  <p class="mt-1 ml-2 grey--text">
                    ({{ place.ratings_amount }})
                  </p>
                </v-row>
              </v-card-text>
            </v-col>
            <v-col cols="1" class="d-flex align-center justify-center">
              <v-icon x-large> mdi-chevron-right </v-icon>
            </v-col>
          </v-row>
        </v-card>
      </v-row>
    </div>
    <div v-else>
      <p class="text-h6 text-center">Brak danych</p>
    </div>
  </div>
</template>
<script>
import { axiosAPI } from "@/axiosAPI";
import { mapState } from "vuex";
export default {
  data() {
    return {
      places: [],
    };
  },
  computed: {
    ...mapState({
      user: (state) => state.user.username,
    }),
  },
  async created() {
    await this.getPlaces();
  },
  methods: {
    async getPlaces() {
      await axiosAPI.get(`/api/places/?user=${this.user}`).then((res) => {
        this.places = res.data;
      });
    },
    capitalizeFirstLetter(string) {
      return string[0].toUpperCase() + string.slice(1);
    },
  },
};
</script>
<style scoped>
.v-rating >>> button {
  padding: 8px 1px;
}
</style>

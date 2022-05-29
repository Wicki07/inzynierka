<template>
  <div class="pt-5">
    <v-row class="mt-8">
      <v-col cols="7">
        <v-autocomplete
          v-model="select"
          :items="items"
          :search-input.sync="search"
          item-text="label"
          return-object
          label="Lokalizacja"
          solo
        >
          <template #no-data>
            <v-list-item>
              <v-list-item-content>
                <v-list-item-title> Brak danych </v-list-item-title>
              </v-list-item-content>
            </v-list-item>
          </template>
        </v-autocomplete>
      </v-col>
      <v-col cols="2">
        <v-select
          v-model="distance"
          :items="distnces"
          label="Dystans"
          solo
        ></v-select>
      </v-col>
      <v-col cols="3">
        <v-btn
          large
          color="customPrimary"
          class="text-subtitle-1 font-weight-medium white--text"
          @click="goToList"
        >
          Wyszukaj
        </v-btn>
      </v-col>
    </v-row>
    <v-row class="ma-5 ma-md-0">
      <v-col cols="12" md="8" class="px-4">
        <v-card-title v-if="state"
          >Województwo {{ capitalizeFirstLetter(state) }}</v-card-title
        >
        <v-row class="mt-3 mb-3" v-for="place of places" :key="place.id">
          <v-card class="mx-auto" @click="() => {$router.push({ name: 'place', params: { place: place, title: place.title.replace(/\s/g, '-') + `-${place.id}` } })}">
            <v-row>
              <v-col cols="0" md="4">
                <v-img
                  class="rounded rounded-r-0"
                  src="https://cdn.vuetifyjs.com/images/cards/sunshine.jpg"
                  height="200px"
                ></v-img>
              </v-col>
              <v-col cols="8">
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
            </v-row>
          </v-card>
        </v-row>
      </v-col>
      <v-col cols="4" class="d-none d-md-flex px-4 flex-column">
        <p class="v-card__title">Wybierz Województwo</p>
        <v-list>
          <v-list-item-group>
            <v-list-item
              style="min-height: 35px"
              v-for="(item, i) in states"
              :key="i"
              :to="`${item}`"
            >
              <v-list-item-content class="py-0">
                <v-list-item-title class="text-body-1"
                  >Województwo {{ item }}</v-list-item-title
                >
              </v-list-item-content>
              <v-list-item-action>
                <v-btn icon>
                  <v-icon color="grey lighten-1">mdi-chevron-right</v-icon>
                </v-btn>
              </v-list-item-action>
            </v-list-item>
          </v-list-item-group>
        </v-list>
      </v-col>
    </v-row>
  </div>
</template>
<script>
import { axiosAPI } from "@/axiosAPI";
import locationSearch from "../mixins/locationSearch";
export default {
  props: {
    state: {
      type: String,
      default() {
        return null;
      },
    },
  },
  mixins: [locationSearch],
  data() {
    return {
      places: [],
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
  watch: {
    state() {
      this.getPlaces();
    },
  },
  async created() {
    await this.getPlaces()
    window.scrollTo(0,0);
  },
  methods: {
    async getPlaces() {
      if (this.state) {
        await axiosAPI.get(`/api/places/?state=${this.state}`).then((res) => {
          this.places = res.data;
        });
      } else {
        await axiosAPI
          .get(
            `/api/placesbylocalization/?lat=${this.$route.query.lat}&lon=${this.$route.query.lon}&distance=${this.$route.query.distance}`
          )
          .then((res) => {
            this.places = res.data;
          });
      }
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

<template>
  <v-container class="d-flex justify-center mt-5 flex-column">
    <v-row class="d-flex justify-center mt-5 flex-column" id="LacatioSearch">
      <p class="text-h4 mx-auto">Wyszukaj wspaniałe miejsca przy pomocy</p>
      <v-col>
        <v-row>
          <v-col cols="12" class="text-center">
            <p class="text-h5 mx-auto">Lokalizacji</p>
          </v-col>
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
              label="Solo field"
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
      </v-col>
    </v-row>
    <v-row id="devider" class="mt-8">
      <v-col cols="5.5" class="d-flex align-center"
        ><v-divider></v-divider
      ></v-col>
      <v-col cols="1" class="text-center text-h6 font-weight-medium">LUB</v-col>
      <v-col cols="5.5" class="d-flex align-center"
        ><v-divider></v-divider
      ></v-col>
    </v-row>
    <v-row class="d-flex justify-center mt-5 flex-column" id="stateChoose">
      <v-col cols="12" class="text-center">
        <p class="text-h5 mx-auto">Wyboru województwa</p>
      </v-col>
      <v-row class="mb-5">
        <v-col
          v-for="(state, index) of states"
          :key="index"
          cols="12"
          lg="3"
          sm="6"
        >
          <v-img
            class="rounded align-center img"
            :src="state.image"
            height="200px"
            @click="$router.push(`posts/list/${state.state}`)"
          >
            <template>
              <div class="text-center text-h6 white--text">Województwo</div>
              <div class="text-center text-h6 white--text">
                {{ state.state }}
              </div>
              <div class="text-center text-subtitle-2 white--text">
                {{ `Ilość miejsc: ${state.amount}` }}
              </div>
            </template>
          </v-img>
        </v-col>
      </v-row>
    </v-row>
    <v-row class="my-8">
      <v-divider></v-divider>
    </v-row>
    <v-row class="d-flex justify-center flex-column mb-5" id="about">
      <p class="text-h4 mb-8 mx-auto">Dlaczego warto poznać swoją okolicę</p>
      <p class="text-body text-center mx-auto">
        Na współczesnego człowieka narzucone jest wiele wyzwań. Szczególnie w
        mieście gdzie tempo życia jest zdecydowanie większe oraz panuje
        wszechobecny hałas. Od blisko 30 lat obserwuje się w Polsce zjawisko
        jakim jest dezurbanizacja czyli zmniejszanie się liczby ludności
        szczególnie dużych miast na rzecz wsi. Przyczyną takiego stanu rzeczy
        jest poszukiwanie przez mieszkańców aglomeracji spokojniejszego i
        zdrowszego życia poza granicami ich miejsca zamieszkania. Ludzie obecnie
        częściej podejmują decyzje na podstawie obranej ścieżki zawodowej.
        Popularność zyskują przeprowadzki w poszukiwaniu pracy lub odpowiednich
        kwalifikacji np. na studia. Ciągłe zmiany i dążenie do sukcesu mogą
        doprowadzić do zaburzenia równowagi psychicznej jak i fizycznej oraz do
        odizolowania się od społeczeństwa. Aby nadążyć za współczesnym światem
        należy zadbać o odpowiedni odpoczynek. Natura jest idealnym miejscem
        gdzie można odpocząć oraz uspokoić zabiegane myśli. Dlatego warto
        wiedzieć gdzie takiego wypoczynku szukać.
      </p>
    </v-row>
  </v-container>
</template>

<script>
import locationSearch from "./posts/mixins/locationSearch";
import { axiosAPI } from "@/axiosAPI";

export default {
  name: "Main",

  mixins: [locationSearch],
  data: () => ({
    distance: 5,
    distnces: [
      {
        text: "+5km",
        value: 5,
      },
      {
        text: "+10km",
        value: 10,
      },
      {
        text: "+15km",
        value: 15,
      },
      {
        text: "+20km",
        value: 20,
      },
      {
        text: "+25km",
        value: 25,
      },
      {
        text: "+30km",
        value: 30,
      },
      {
        text: "+35km",
        value: 35,
      },
      {
        text: "+40km",
        value: 40,
      },
      {
        text: "+45km",
        value: 45,
      },
      {
        text: "+50km",
        value: 50,
      },
    ],
    states: [
      { state: "dolnośląskie" },
      { state: "kujawsko-pomorskie" },
      { state: "łódzkie" },
      { state: "lubeskie" },
      { state: "lubuskie" },
      { state: "małopolskie" },
      { state: "mazowieckie" },
      { state: "opolskie" },
      { state: "podkarpackie" },
      { state: "podlaskie" },
      { state: "pomorskie" },
      { state: "śląskie" },
      { state: "świętokrzyskie" },
      { state: "warmińsko-mazurskie" },
      { state: "wielkopolskie" },
      { state: "zachodniopomorskie" },
    ],
    search: null,
    select: null,
    items: [],
  }),
  watch: {
    search(val) {
      val && val !== this.select && this.querySelections(val);
    },
  },
  computed: {
    width() {
      return window.innerWidth;
    },
  },
  async created() {
    await axiosAPI.get("/api/mainscreenposts").then((response) => {
      const fomatedArray = response.data.reduce(
        (acc, curr) => ((acc[curr.state.split(" ")[1]] = curr), acc),
        {}
      );
      this.states = this.states.map((val) => ({
        ...val,
        amount: fomatedArray[val.state]?.count ? fomatedArray[val.state].count : 0,
        image: fomatedArray[val.state]?.attachment ? `${process.env.VUE_APP_BACKEND_URL}${fomatedArray[val.state].attachment}` : "https://cdn.vuetifyjs.com/images/cards/sunshine.jpg" 
      }))
    });
  },
  methods: {
    capitalizeFirstLetter(string) {
      return string[0].toUpperCase() + string.slice(1);
    },
    async goToList() {
      if (this.select) {
        const results = await this.provider.search({ query: this.search });
        this.select = results[0];
      }
      this.$router.push({
        path: "posts/list",
        query: {
          lat: this.select.y,
          lon: this.select.x,
          distance: this.distance,
        },
      });
    },
    async querySelections(val) {
      const results = await this.provider.search({ query: val });
      this.items = results.map((item) => ({
        ...item,
        fullLabel: item.label,
        label:
          item.label.length < 70 ? item.label : `${item.label.slice(0, 70)}...`,
      }));
    },
  },
};
</script>
<style lang="css" scoped>
.img :hover {
  cursor: pointer;
}
</style>

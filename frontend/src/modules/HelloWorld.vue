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
            <v-text-field label="Lokalizacja" solo></v-text-field>
          </v-col>
          <v-col cols="2">
            <v-select
              v-model="distnce"
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
            src="https://cdn.vuetifyjs.com/images/cards/sunshine.jpg"
            height="200px"
            @click="$router.push(`posts/list/${state}`)"
            >
              <template>
                <div class="text-center text-h6 white--text">Województwo</div>
                <div class="text-center text-h6 white--text">{{state}}</div>
                <div class="text-center text-subtitle-2 white--text">x miejsc</div>
              </template>
            </v-img
          >
        </v-col>
      </v-row>
    </v-row>
    <v-row class="my-8">
      <v-divider></v-divider>
    </v-row>
    <v-row class="d-flex justify-center flex-column mb-5" id="about">
      <p class="text-h4 mb-8 mx-auto">Dlaczego warto poznać swoją okolicę</p>
      <p class="text-body text-center mx-auto">Na współczesnego człowieka narzucone jest wiele wyzwań. Szczególnie w mieście gdzie tempo życia jest zdecydowanie większe oraz panuje wszechobecny hałas. Od blisko 30 lat obserwuje się w Polsce zjawisko jakim jest dezurbanizacja czyli zmniejszanie się liczby ludności szczególnie dużych miast na rzecz wsi. Przyczyną takiego stanu rzeczy jest poszukiwanie przez mieszkańców aglomeracji spokojniejszego i zdrowszego życia poza granicami ich miejsca zamieszkania. Ludzie obecnie częściej podejmują decyzje na podstawie obranej ścieżki zawodowej. Popularność zyskują przeprowadzki w poszukiwaniu pracy lub odpowiednich kwalifikacji np. na studia. Ciągłe zmiany i dążenie do sukcesu mogą doprowadzić do zaburzenia równowagi psychicznej jak i fizycznej oraz do odizolowania się od społeczeństwa. Aby nadążyć za współczesnym światem należy zadbać o odpowiedni odpoczynek. Natura jest idealnym miejscem gdzie można odpocząć oraz uspokoić zabiegane myśli. Dlatego warto wiedzieć gdzie takiego wypoczynku szukać.</p>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: "HelloWorld",

  data: () => ({
    distnce: 5,
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
  }),
  computed: {
    width() {
      return window.innerWidth;
    },
  },
  methods: {
    capitalizeFirstLetter(string) {
      return string[0].toUpperCase() + string.slice(1);
    },
  },
};
</script>
<style lang="css" scoped>
.img :hover {
  cursor: pointer;
}
</style>
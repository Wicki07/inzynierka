<template>
  <div>
    <v-card class="ma-5 pa-5">
      <v-card-title v-if="state">Województwo {{ capitalizeFirstLetter(state) }}</v-card-title>
      <v-row>
        Tu będzie lista miejsc
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
        return null
      }
    }
  },
  data() {
    return {
      places: []
    };
  },
  async created() {
    await axiosAPI.get(`/api/places?state=${this.state}`)
  },
  methods: {
    capitalizeFirstLetter(string) {
      return string[0].toUpperCase() + string.slice(1);
    },
  },
};
</script>
<style scoped></style>

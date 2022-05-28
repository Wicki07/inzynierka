<template>
  <div style="height: 350px">
    <l-map
      @ready="mapReady()"
      ref="myMap"
      id="map"
      style="height: 80%; width: 100%"
      :zoom="zoom"
      :center="center"
      @click="handleClick"
      ><l-marker
        v-if="markerAdded"
        :draggable="true"
        :lat-lng="markerLatLng"
      ></l-marker>
      <l-tile-layer :url="url" :attribution="attribution"></l-tile-layer>
      <v-locatecontrol
        :options="{
          position: 'topright',
          strings: {
            title: 'Twoja lokalizacja',
          },
        }"
      />
    </l-map>
  </div>
</template>

<script>
import { GeoSearchControl, OpenStreetMapProvider } from "leaflet-geosearch";
import L from "leaflet";
import { LMap, LTileLayer, LMarker } from "vue2-leaflet";
import Vue2LeafletLocatecontrol from "vue2-leaflet-locatecontrol";
import axios from "axios";

// Icon fix
delete L.Icon.Default.prototype._getIconUrl;
L.Icon.Default.mergeOptions({
  iconRetinaUrl: require("leaflet/dist/images/marker-icon-2x.png"),
  iconUrl: require("leaflet/dist/images/marker-icon.png"),
  shadowUrl: require("leaflet/dist/images/marker-shadow.png"),
});

export default {
  components: {
    LMap,
    LTileLayer,
    LMarker,
    "v-locatecontrol": Vue2LeafletLocatecontrol,
  },
  props: {
    localization: {
      type: String,
      default: "",
    }
  },
  data() {
    return {
      url: "https://{s}.basemaps.cartocdn.com/rastertiles/voyager_labels_under/{z}/{x}/{y}{r}.png",
      attribution:
        '&copy; <a target="_blank" href="http://osm.org/copyright">OpenStreetMap</a> contributors',
      zoom: 10,
      center: [47.41322, -1.219482],
      bounds: null,
      markerLatLng: [0, 0],
      markerAdded: false,
      markerLabel: "",
    };
  },
  async created(){
    if(this.localization) {
      await this.assignMarker(this.localization.split(',')[0], this.localization.split(',')[1])
    }
  },
  watch:{
    async localization(newVal) {
      await this.assignMarker(newVal.split(',')[0], newVal.split(',')[1])
    }
  },
  methods: {
    async handleClick(e) {
      await this.assignMarker(e.latlng.lat, e.latlng.lng)
    },
    mapReady() {
      var map = this.$refs.myMap.mapObject;
      const search = new GeoSearchControl({
        provider: new OpenStreetMapProvider({
        params: {
          "accept-language": "pl", 
          addressdetails: 1,
        },
      }),
        style: "bar",
        searchLabel: "Wpisz adres",
      });
      search.addMarker = (t) => {
        this.markerAdded = true;
        this.markerLatLng = [t.y, t.x];
        this.center = [t.y, t.x];
        this.markerLabel = t.raw.address;
      };
      map.addControl(search);
    },
    async assignMarker(lat, lng) {
      const provider = new OpenStreetMapProvider({
        params: {
          "accept-language": "pl", 
          addressdetails: 1,
        },
      });
      this.markerAdded = true;
      this.markerLatLng = [lat, lng];
      this.center = [lat, lng];      
      const results = await provider.search({
        query: lat + ", " + lng,
      });
      this.markerLabel = results[0].raw.address;
    }
  },
};
</script>
<style>
@import "~leaflet/dist/leaflet.css";
@import "https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css";
</style>

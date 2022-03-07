<template>
  <div style="height: 350px">
    <l-map
      @ready="doSomethingOnReady()"
      ref="myMap"
      id="map"
      style="height: 80%; width: 100%"
      :zoom="zoom"
      :center="center"
      @click="handleClick"
    ><l-marker v-if="markerAdded" :draggable="true" :lat-lng="markerLatLng"></l-marker>
      <l-tile-layer :url="url" :attribution="attribution"></l-tile-layer>
    </l-map>
    <div ref="testdiv"></div>
  </div>
</template>

<script>
import {GeoSearchControl, OpenStreetMapProvider } from 'leaflet-geosearch';
import L from "leaflet";
import { LMap, LTileLayer, LMarker } from "vue2-leaflet";

export default {
  components: {
    LMap,
    LTileLayer,
    LMarker
  },
  data() {
    return {
      url: "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
      attribution:
        '&copy; <a target="_blank" href="http://osm.org/copyright">OpenStreetMap</a> contributors',
      zoom: 3,
      center: [47.41322, -1.219482],
      bounds: null,
      markerLatLng: [0, 0],
      markerAdded: false
    };
  },
  methods: {
    handleClick(e) {
      this.markerAdded = true
      this.markerLatLng = [e.latlng.lat, e.latlng.lng]
      this.center = [e.latlng.lat, e.latlng.lng]
      console.log(this.$refs.myMap.mapObject)
    },
    doSomethingOnReady() {
      var map = this.$refs.myMap.mapObject;
      L.tileLayer("//{s}.tile.openstreetmap.org/{z}/{x}/{y}.png").addTo(map);
      const search = new GeoSearchControl({
        provider: new OpenStreetMapProvider(),
      });
      search.addMarker = (t) => {
      this.markerAdded = true
      this.markerLatLng = [t.y, t.x]
      this.center = [t.y, t.x]
      }
      console.log(map)
      console.log(search)
      console.log(this.$refs.testdiv)
      map.addControl(search);
    },
  },
};
</script>

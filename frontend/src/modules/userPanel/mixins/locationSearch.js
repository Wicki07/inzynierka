
import { GeoSearchControl, OpenStreetMapProvider } from "leaflet-geosearch";
export default {
  data() {
    return {
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
      search: null,
      select: null,
      items: [],
      provider: new OpenStreetMapProvider({
        params: {
          "accept-language": "pl",
          addressdetails: 1,
        },
      }),
    };
  },
  watch: {
    search(val) {
      val && val !== this.select && this.querySelections(val);
    },
  },
  methods: {
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

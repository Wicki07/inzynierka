import Vue from "vue";
import Vuetify from "vuetify/lib/framework";

Vue.use(Vuetify);

export default new Vuetify({
  theme: {
    themes: {
      light: {
        primary: '#1976D2',
        secondary: '#424242',
        accent: '#82B1FF',
        error: '#FF5252',
        info: '#2196F3',
        success: '#4CAF50',
        customPrimary: '#007bff',
        customSecondary: '#b44545',
        customAccent: '#999',
        warning: '#FFC107',
        warning: '#FFC107',
      },
    },
  },
});

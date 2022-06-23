<template>
  <div class="mt-16">
    <p class="text-h4">{{ user }}</p>
    <v-list subheader>
      <v-subheader>Ustawienia</v-subheader>

      <v-list-item
        v-for="item in settings"
        :key="item.title"
        @click="() => {$router.push(item.link)}"
      >
        <v-list-item-avatar>
          <v-icon color="grey">{{item.icon}}</v-icon>
        </v-list-item-avatar>
        <v-list-item-content>
          <v-list-item-title v-text="item.title"></v-list-item-title>
        </v-list-item-content>
        <v-list-item-icon>
          <v-icon color="grey">
            mdi-chevron-right
          </v-icon>
        </v-list-item-icon>
      </v-list-item>
    </v-list>
  </div>
</template>
<script>
import { axiosAPI } from "@/axiosAPI";
import { mapState } from "vuex";
export default {
  data() {
    return {
      settings: [
        {
          title: "Zmień hasło",
          icon: "mdi-lock",
          link: "settings/passwordchange"
        },
        {
          title: "Zarządzaj postami",
          icon: "mdi-map-marker-radius",
          link: "settings/manageposts"
        },
        // {
        //   title: "Zarządaj komentarzami",
        //   icon: "mdi-comment-multiple",
        //   link: "settings/managecomments"
        // }
      ]
    };
  },
  computed: {
    ...mapState({
      user: (state) => state.user.username,
    }),
  },
  methods: {},
};
</script>
<style scoped></style>

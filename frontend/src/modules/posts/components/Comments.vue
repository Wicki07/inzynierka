<template>
  <v-container>
    <v-row id="comments">
      <v-col cols="12">
        <v-card-title>Komentarze</v-card-title>
      </v-col>
      <comment-field
        :place="place"
        :comments="comments"
        @replay="replay"
        @getComments="getComments"
      ></comment-field>
      <v-col cols="12" v-if="user">
        <v-expansion-panels v-model="commentPanel" flat tile popout inset>
          <v-expansion-panel @click="responseTo = null">
            <v-expansion-panel-header class="primary--text"
              >Dodaj komentarz</v-expansion-panel-header
            >
            <v-expansion-panel-content>
              <div class="mt-6">
                <v-row class="elevation-10 flex-column mx-0">
                  <v-row
                    style="height: 40px"
                    class="primary lighten-5 rounded-lg rounded-b-0 align-center pl-3 mx-0"
                  >
                  </v-row>
                  <v-col class="align-center pl-5 mx-0">
                    <v-textarea
                      v-model="newComment"
                      label="Twój komentarz"
                      rows="3"
                    ></v-textarea>
                    <v-rating
                      v-model="rate"
                      empty-icon="mdi-star-outline"
                      full-icon="mdi-star"
                      half-icon="mdi-star-half-full"
                      color="yellow darken-3"
                      background-color="grey darken-1"
                      hover
                      half-increments
                      length="5"
                      small
                    ></v-rating>
                    <v-btn small text color="primary" @click="saveComment()"
                      >Zatwierdź</v-btn
                    >
                  </v-col>
                </v-row>
              </div>
            </v-expansion-panel-content>
          </v-expansion-panel>
        </v-expansion-panels>
      </v-col>
    </v-row>
    <v-overlay :value="overlay">
      <v-progress-circular indeterminate size="64"></v-progress-circular>
    </v-overlay>
  </v-container>
</template>
<script>
import { axiosAPI } from "@/axiosAPI";
import CommentField from "./CommentField.vue";
import { mapState } from "vuex";

export default {
  components: { CommentField },
  props: {
    place: {
      type: Number,
      default() {
        return 0;
      },
    },
  },
  data() {
    return {
      comments: [],
      commentPanel: false,
      newComment: "",
      responseTo: null,
      parentCommentContent: "",
      overlay: false,
      rate: null,
    };
  },
  computed: {
    ...mapState({
      user: (state) => state.user.username,
    }),
  },
  watch: {
    place() {
      this.cancelComment();
      this.getComments();
    },
  },
  async created() {
    await this.getComments();
  },
  async mounted() {
    await this.getComments();
  },
  methods: {
    replay(idx, content) {
      this.responseTo = idx;
      this.commentPanel = 0;
      this.parentCommentContent = content;
    },
    async getComments() {
      this.overlay = true;
      await axiosAPI.get(`/api/comments/?post=${this.place}`).then((res) => {
        this.comments = res.data;
      });
      this.overlay = false;
      this.cancelComment();
    },
    async saveComment() {
      this.overlay = true;
      await axiosAPI
        .post("/api/comments/", {
          comment: this.newComment,
          post: +this.place,
          parent_com: +this.responseTo,
          rate: this.rate,
          user: this.user,
        })
        .then(() => {
          this.getComments();
        });
      this.overlay = false;
      this.cancelComment();
    },
    cancelComment() {
      this.commentPanel = false;
      this.newComment = "";
      this.responseTo = null;
      this.parentCommentContent = "";
    },
  },
};
</script>
<style>
.my-select .v-select__selections .v-select__selection--disabled {
  color: #fff !important;
}
</style>

<template>
  <v-container>
    <v-row id="comments">
      <v-col cols="12">
        <v-card-title>Komentarze</v-card-title>
      </v-col>
      <comment-field :comments="comments" @replay="replay"></comment-field>
      <v-col cols="12">
        <v-expansion-panels v-model="commentPanel" flat tile popout inset>
          <v-expansion-panel @click="responseTo = null">
            <v-expansion-panel-header
              style="background-color: rgba(52, 94, 107, 0.8) !important"
            >Dodaj komentarz</v-expansion-panel-header>
            <v-expansion-panel-content
              style="background-color: rgba(52, 94, 107, 0.8) !important"
            >
              <div v-if="parentCommentContent">
                Odpowiedz na: {{ parentCommentContent }}
              </div>
              <v-textarea
                v-model="newComment"
                rows="2"
                :auto-grow="true"
                filled
                rounded
                dense
              ></v-textarea>
              <v-btn @click="saveComment">Zapisz</v-btn>
              <v-btn @click="cancelComment">Anuluj</v-btn>
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
    };
  },
  computed: {
    ...mapState({
      user: (state) => state.user.username
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
          rate: null,
          user: this.user
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

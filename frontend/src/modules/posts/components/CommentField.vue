<template>
  <v-row id="comments">
    <v-col
      v-for="(comment, idx) of commentsLocal"
      :key="comment.id"
      cols="12"
      class="pr-0"
    >
      <v-col class="elevation-10 mx-0 rounded-lg rounded-b-0 px-0">
        <v-row
          style="height: 40px"
          class="primary lighten-5 rounded-lg rounded-b-0 align-center pl-3 mx-0"
        >
          <p class="primary--text align-center mb-0 font-weight-bold">
            {{ comment.name }}
          </p>
          <v-spacer />
          <p
            class="primary--text text--lighten-1 text-body-2 align-center mb-0 mr-3"
          >
            {{ new Date(comment.created_at).toLocaleString() }}
          </p>
        </v-row>
        <v-row class="align-center pl-5 mx-0 mt-0 pt-3 ">
          <p>{{ comment.comment }}</p>
        </v-row>
        <v-row class="align-center pr-5 mx-0 mt-0 pt-3">
          <v-spacer></v-spacer>
          <v-btn v-if="user" small text color="primary" @click="replay(idx)">Odpowiedz</v-btn>
        </v-row>
      </v-col>
      <v-row v-if="comment.child_comments" class="mr-0 ml-8 mt-2 mb-0">
        <v-col cols="1">
          <v-divider
            class="primary lighten-3 rounded-lg"
            style="border-width: 2px"
            vertical
          ></v-divider>
        </v-col>
        <v-col cols="11">
          <comment-field
            :place="place"
            :comments="comment.child_comments"
            :offset="offset + 1"
            :parent-comment="comment.id"
            @replay="replay"
            @getComments="$emit('getComments')"
          ></comment-field>
        </v-col>
      </v-row>
      <div v-if="comment.replay" class="mt-6">
        <v-row class="elevation-10 flex-column mx-0">
          <v-row
            style="height: 40px"
            class="primary lighten-5 rounded-lg rounded-b-0 align-center pl-3 mx-0"
          >
            <p class="align-center mb-0 mr-1">
              Odpowiedz na komentarz użytkownika:
            </p>
            <p class="primary--text align-center mr-1 mb-0 font-weight-bold">
              {{ comment.name }},
            </p>
            <p class="align-center mb-0">
              {{ comment.comment.length < 70 ? comment.comment : `${comment.comment.slice(0, 70)}...` }}
            </p>
          </v-row>
          <v-col class="align-center pl-5 mx-0">
            <v-textarea v-model="newComment" label="Twój komentarz" rows="3"></v-textarea>
          <v-btn small text color="primary" @click="saveComment()">Zatwierdź</v-btn>
          </v-col>
        </v-row>
      </div>
    </v-col>
  </v-row>
</template>
<script>
import { axiosAPI } from "@/axiosAPI";
import { mapState } from "vuex";
export default {
  name: "CommentField",
  props: {
    offset: {
      type: Number,
      default() {
        return 0;
      },
    },
    comments: {
      type: Array,
      default() {
        return [];
      },
    },
    parentComment: {
      type: Number,
      default() {
        return -1;
      },
    },
    place: {
      type: Number,
      default() {
        return 0;
      },
    },
  },
  data() {
    return {
      commentsLocal: [],
      commentPanel: false,
      newComment: "",
      responseTo: "",
    };
  },
  computed: {
    ...mapState({
      user: (state) => state.user.username
    }),
  },
  watch: {
    comments(val) {
      this.commentsLocal = val;
    },
  },
  mounted() {
    this.commentsLocal = this.comments;
  },
  methods: {
    async saveComment() {
      await axiosAPI
        .post("/api/comments/", {
          comment: this.newComment,
          post: +this.place,
          parent_com: +this.responseTo,
          rate: null,
          user: "marik1234"
        })
        .then(() => {
          this.$emit("getComments")
        });
    },
    replay(localIndex) {
      this.commentsLocal = this.commentsLocal.map((comment, index) => {
        if (index === localIndex) {
          this.responseTo = comment.id;
          return {
            ...comment,
            replay: true,
          };
        } else {
          return comment;
        }
      });
    },
  },
};
</script>
<style></style>

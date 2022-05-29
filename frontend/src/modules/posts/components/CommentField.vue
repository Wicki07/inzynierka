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
          <v-rating
            v-if="comment.rate"
            readonly
            empty-icon="mdi-star-outline"
            full-icon="mdi-star"
            half-icon="mdi-star-half-full"
            color="yellow darken-3"
            background-color="grey darken-1"
            hover
            half-increments
            length="5"
            :value="comment.rate"
            small
          ></v-rating>
          <v-spacer />
          <p
            class="primary--text text--lighten-1 text-body-2 align-center mb-0 mr-3"
          >
            {{ new Date(comment.created_at).toLocaleString() }}
          </p>
        </v-row>
        <v-row class="align-center pl-5 mx-0 mt-0 pt-3">
          <p>{{ comment.comment }}</p>
        </v-row>
        <v-row class="align-center pr-5 mx-0 mt-0 pt-3">
          <v-spacer></v-spacer>
          <v-btn
            v-if="user === comment.name"
            small
            text
            color="primary"
            @click="replay(idx, 'edit')"
            >Edytuj</v-btn
          >
          <v-btn
            v-if="user"
            small
            text
            color="primary"
            @click="replay(idx, 'replay')"
            >Odpowiedz</v-btn
          >
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
      <div v-if="comment.replay || comment.edit" class="mt-6">
        <v-row class="elevation-10 flex-column mx-0">
          <v-row
            v-if="comment.replay"
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
              {{
                70 > comment.comment.length
                  ? comment.comment
                  : `${comment.comment.slice(0, 70)}...`
              }}
            </p>
          </v-row>
          <v-row
            v-else
            style="height: 40px"
            class="primary lighten-5 rounded-lg rounded-b-0 align-center pl-3 mx-0"
          >
            <p class="align-center mb-0 mr-1">Edycja komentarza</p>
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
          </v-row>
          <v-col class="align-center pl-5 mx-0">
            <v-textarea
              v-model="newComment"
              label="Twój komentarz"
              rows="3"
            ></v-textarea>
            <v-btn small text color="primary" @click="saveComment()"
              >Zatwierdź</v-btn
            >
            <v-btn small text color="error" @click="deleteComment(comment.id)"
              >Usuń</v-btn
            >
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
      editedComment: null,
      rate: null,
    };
  },
  computed: {
    ...mapState({
      user: (state) => state.user.username,
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
          rate: this.rate,
          user: "marik1234",
          editedComment: this.editedComment,
        })
        .then(() => {
          this.$emit("getComments");
        });
    },
    replay(localIndex, key) {
      this.commentsLocal = this.commentsLocal.map((comment, index) => {
        if (index === localIndex) {
          this.responseTo = comment.id;
          if (key === "edit") {
            this.newComment = comment.comment;
            this.editedComment = comment.id;
            this.rate = comment.rate;
          }
          return {
            ...comment,
            [key]: true,
          };
        } else {
          return comment;
        }
      });
    },
    async deleteComment(id) {
      await axiosAPI
        .delete(`/api/comments/${id}`)
        .then(() => {
          this.$emit("getComments");
        })
    },
  },
};
</script>
<style></style>

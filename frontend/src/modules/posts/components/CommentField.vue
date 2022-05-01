<template>
  <v-row id="comments">
    <v-col
      v-for="(comment, idx) of commentsLocal"
      :key="comment.id"
      cols="12"
      class="pr-0 mt-5"
    >
      <v-row class="elevation-10 flex-column mx-0">
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
        <v-row class="align-center pl-5 mx-0">
          <p>{{ comment.comment }}</p>
        </v-row>
      </v-row>
      <v-row v-if="comment.child_comments" class="mr-0 ml-8 mt-5 mb-0">
        <v-col cols="1">
          <v-divider class="primary lighten-3 rounded-lg" style="border-width: 2px;" vertical></v-divider>
        </v-col>
        <v-col cols="11">
          <comment-field
            :comments="comment.child_comments"
            :offset="offset + 1"
            :parent-comment="comment.id"
            @replay="replay"
          ></comment-field>
        </v-col>
      </v-row>
      <div v-if="comment.replay">
        <v-textarea
          class="testowa"
          v-model="newComment"
          rows="2"
          :auto-grow="true"
          filled
          rounded
          dense
        ></v-textarea>
        <v-btn @click="saveComment">Zapisz</v-btn>
        <v-btn @click="cancelComment">Anuluj</v-btn>
      </div>
    </v-col>
    <!-- <v-col cols="12">
      <v-expansion-panels v-model="commentPanel" flat tile popout inset>
        <v-expansion-panel>
          <v-expansion-panel-header>Dodaj komentarz</v-expansion-panel-header>
          <v-expansion-panel-content>
            <v-textarea
              rows="2"
              :auto-grow="true"
              filled
              rounded
              dense
              v-model="newComment"
            ></v-textarea>
            <v-btn @click="saveComment">Zapisz</v-btn>
            <v-btn @click="cancelComment">Anuluj</v-btn>
          </v-expansion-panel-content>
        </v-expansion-panel>
      </v-expansion-panels>
    </v-col> -->
  </v-row>
</template>
<script>
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
  },
  data() {
    return {
      commentsLocal: [],
      commentPanel: false,
      newComment: "",
      responseTo: "",
    };
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
    replay(idx, content, localIndex) {
      console.log(this.commentsLocal);
      console.log(localIndex);
      this.commentsLocal = this.commentsLocal.map((comment, index) => {
        if (index === localIndex) {
          return {
            ...comment,
            replay: true,
          };
        } else {
          return comment;
        }
      });
      // this.$emit("replay", idx, content);
    },
  },
};
</script>
<style></style>

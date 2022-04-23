<template>
  <v-row id="comments">
    <v-col v-for="comment of commentsLocal" :key="comment.id" cols="12">
      <v-textarea
        rows="2"
        :auto-grow="true"
        :value="comment.comment"
        readonly
        persistent-hint
        filled
        rounded
        dense
        :hint="`${comment.name} ${new Date(
          comment.created_at
        ).toLocaleString()}`"
        @click="replay(comment.id, comment.comment)"
      ></v-textarea>
      <comment-field
        :comments="comment.child_comments"
        :offset="offset + 1"
        :parent-comment="comment.id"
        @replay="replay"
      ></comment-field>
      <div v-if="comment.replay">
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
    replay(idx, content) {
      this.$emit("replay", idx, content);
    },
  },
};
</script>
<style>
#comments {
  margin-right: 0px !important;
  margin-left: 25px !important;
}
#comments .col {
  padding: 0px !important;
}
</style>

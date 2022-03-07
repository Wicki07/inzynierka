<template>
  <v-container>
    <v-card>
      <v-text-field
        class="mt-5"
        v-model="localization"
        label="Lokalizacja"
      ></v-text-field>
      <v-text-field
        class="mt-5"
        v-model="category"
        label="Kategoria"
      ></v-text-field>
      <v-textarea class="mt-5" v-model="description" label="Opis"></v-textarea>
      <div @dragover="dragover" @dragleave="dragleave" @drop="drop">
        <v-file-input
          accept="image/png, image/jpeg, image/bmp, image/img"
          prepend-icon="mdi-camera"
          ref="imginput"
          chips
          multiple
          label="Zdjęcia"
          :rules="imageRules"
          v-model="images"
          @change="onAddFiles"
        ></v-file-input>
      </div>
      <v-btn color="success" @click="addPost">dodaj </v-btn>
    </v-card>
    <map-test></map-test>
  </v-container>
</template>
<script>
import { axiosAPI } from "@/axiosAPI";
import MapTest from "./MapTest.vue";
export default {
  components: {
    MapTest,
  },
  data() {
    return {
      localization: "",
      category: "",
      description: "",
      images: [],
      convertedImages: [],
      allowedTypes: "image/png, image/jpeg, image/bmp, image/img",
      imageRules: [
        (v) => {
          var hasDuplicates = false;
          var checkedValues = [];
          v.forEach((value) => {
            if (checkedValues.some((val) => val.name == value.name)) {
              hasDuplicates = true;
            }
            checkedValues.push(value);
          });
          return !hasDuplicates || "Dodano już podany plik";
        },
        (v) =>
          !v ||
          !v.some((value) => !this.allowedTypes.includes(value.type)) ||
          "Podano niewłaściwy format pliku. Dopuszczalne formaty: png, jpg, jpeg, bmp, img",
      ],
    };
  },
  methods: {
    addPost() {
      const formData = new FormData();
      formData.append("localization", this.localization);
      formData.append("category", this.category);
      formData.append("description", this.description);
      this.convertedImages.forEach((image) => {
        formData.append("images", image, image.name);
      });
      console.log(formData.getAll("images"));
      axiosAPI
        .post("/api/post", formData, {
          headers: {
            ...axiosAPI.headers,
            "content-type": "multipart/form-data",
          },
        })
        .then((res) => {
          localStorage.setItem("token", res.data.token);
          this.setUser(res.data.user);
        })
        .catch((err) => {
          console.log("err");
          console.log(err);
        });
    },
    onAddFiles(files) {
      if (files.length == 0) {
        this.convertedImages = [];
      }
      files.forEach((file) => {
        const reader = new FileReader();
        reader.readAsArrayBuffer(file);
        const self = this;
        reader.onload = function (event) {
          var blob = new Blob([event.target.result]);
          var blobURL = URL.createObjectURL(blob);
          var image = new Image();
          image.src = blobURL;
          image.onload = async function () {
            var resized = self.resizeMe(image);
            let file = await fetch(resized)
              .then((r) => r.blob())
              .then(
                (blobFile) =>
                  new File([blobFile], self.imgName(), { type: "image/png" })
              );
            self.convertedImages.push(file);
          };
        };
      });
    },
    resizeMe(img) {
      var canvas = document.createElement("canvas");

      var width = img.width;
      var height = img.height;
      var max_width = 800;
      var max_height = 800;
      if (width > height) {
        if (width > max_width) {
          height = Math.round((height *= max_width / width));
          width = max_width;
        }
      } else {
        if (height > max_height) {
          width = Math.round((width *= max_height / height));
          height = max_height;
        }
      }
      canvas.width = width;
      canvas.height = height;
      var ctx = canvas.getContext("2d");
      ctx.drawImage(img, 0, 0, width, height);
      return canvas.toDataURL("image/jpeg", 0.8);
    },
    imgName() {
      var result = "";
      var characters =
        "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";
      var charactersLength = characters.length;
      for (var i = 0; i < 20; i++) {
        result += characters.charAt(
          Math.floor(Math.random() * charactersLength)
        );
      }
      return result;
    },
    dragover(event) {
      event.preventDefault();
      this.$refs.imginput.focus();
    },
    dragleave(event) {
      event.preventDefault();
      this.$refs.imginput.blur();
    },
    drop(event) {
      event.preventDefault();
      this.onAddFiles(Array.from(event.dataTransfer.files));
      this.images.push(...event.dataTransfer.files);
      this.$refs.imginput.validate();
    },
  },
};
</script>
<style scoped></style>

<template>
  <div class="mt-8">
    <v-alert
      v-model="alert"
      :type="alertType"
      dismissible
      style="position: absolute; top: 16px; z-index: 4"
      transition="slide-x-transition"
      >{{ alertMsg }}</v-alert
    >
    <v-btn color="primary" text @click="() => $router.go(-1)">
      <v-icon left> mdi-chevron-left </v-icon>
      Wróć
    </v-btn>
    <p class="text-h4 mt-8">Dodaj miejsce</p>
    <v-form v-model="valid" ref="form">
      <v-select
        v-model="category"
        :items="categories"
        label="Kategoria *"
        :rules="rules"
      ></v-select>
      <v-text-field
        class="mt-5"
        v-model="title"
        label="Tytuł *"
        hint="Nazwa pod jaką inni będą mogli wszyukiwać podane miejsce"
        :rules="rules"
      ></v-text-field>
      <v-textarea
        class="mt-5"
        v-model="description"
        label="Opis *"
        hint="Krótki opis podanego miejsca"
        :rules="rules"
      ></v-textarea>
      <p class="text-subtitle-1 mb-0 mt-4">
        Dodaj zdjęcia lub przeciągnij na pole
      </p>
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
      <v-row class="pa-3" v-if="imagesUrls.length !== 0">
        <v-img
          v-for="(img, idx) in imagesUrls"
          :key="idx"
          max-height="100"
          max-width="160"
          :src="img"
          class="mr-3"
        >
          <v-spacer></v-spacer>
          <v-btn fab x-small color="primary" @click="removeFile(idx)">
            <v-icon dark> mdi-minus </v-icon>
          </v-btn></v-img
        >
      </v-row>
    </v-form>
    <p class="text-subtitle-1 mb-0 mt-4">Podaj lokalizację miejsca</p>
    <localization-select ref="localizationselect" />
    <v-row class="justify-end mb-5">
      <v-btn color="primary lighten-1" @click="addPost">dodaj</v-btn>
    </v-row>
  </div>
</template>
<script>
import { axiosAPI } from "@/axiosAPI";
import LocalizationSelect from "../components/LocalizationSelect.vue";
export default {
  components: {
    LocalizationSelect,
  },
  data() {
    return {
      valid: false,
      localization: "",
      title: "",
      category: "",
      categories: ["Punkt widokowy", "Odpoczynek", "Aktywny wypoczynek"],
      description: "",
      images: [],
      convertedImages: [],
      imagesUrls: [],
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
      rules: [(v) => !!v || "Pole wymagane"],
      alert: false,
      alertMsg: "Coś poszło nie tak! Spróbuj ponownie.",
      alertType: "error",
    };
  },
  created(){
    window.scrollTo(0,0);
  },
  methods: {
    removeFile(idx) {
      this.imagesUrls.splice(idx, 1);
      this.convertedImages.splice(idx, 1);
      this.images.splice(idx, 1);
    },
    addPost() {
      this.$refs.form.validate();
      if (this.valid && this.$refs.localizationselect.markerLabel) {
        const formData = this.preprareFromData();
        this.convertedImages.forEach((image) => {
          formData.append("images", image, image.name);
        });
        axiosAPI
          .post("/api/post", formData, {
            headers: {
              ...axiosAPI.headers,
              "content-type": "multipart/form-data",
            },
          })
          .then(() => {
            this.alertMsg = "Pomyślnie dodano miejsce";
            this.alert = true;
            this.alertType = "success";
            setTimeout(() => {
              this.alert = false;
            }, 5000);
            this.imagesUrls = []
            this.$refs.form.reset();
            this.$refs.localizationselect.markerLabel;
            this.$refs.localizationselect.markerLatLng = [0, 0];
            this.$refs.localizationselect.markerAdded = false;
            this.$refs.localizationselect.markerLabel = "";
          })
          .catch(() => {
            this.alertMsg = "Coś poszło nie tak. Spróbuj ponownie";
            this.alert = true;
            this.alertType = "error";
            setTimeout(() => {
              this.alert = false;
            }, 5000);
          });
      } else {
        this.alertMsg = "Uzupełnij barkujące pola i spróbuj ponownie";
        this.alert = true;
        this.alertType = "error";
        setTimeout(() => {
          this.alert = false;
        }, 5000);
      }
    },
    preprareFromData() {
      const formData = new FormData();
      const markerLabel = this.$refs.localizationselect.markerLabel;
      formData.append(
        "localization",
        this.$refs.localizationselect.markerLatLng
      );
      formData.append("category", this.category);
      formData.append("title", this.title);
      formData.append("description", this.description);
      formData.append("country", markerLabel.country);
      formData.append("post_code", markerLabel.postcode);
      formData.append("state", markerLabel.state);
      formData.append(
        "city",
        markerLabel.city || markerLabel.village || markerLabel.town
      );
      const street = `${markerLabel.road || ""} ${
        markerLabel.house_number || ""
      }`;
      formData.append("street", street.trim());
      return formData;
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
          self.imagesUrls.push(blobURL);
          var image = new Image();
          image.src = blobURL;
          image.onload = async function () {
            var resized = self.resizeMe(image);
            let file = await fetch(resized)
              .then((r) => r.blob())
              .then(
                (blobFile) =>
                  new File([blobFile], self.imgName() + ".jpg", {
                    type: "image/jpeg",
                  })
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

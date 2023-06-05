<template>
  <v-form v-model="valid" ref="form">
    <v-container>
      <v-row>
        <v-col cols="12">
          <v-sheet color="white" elevation="1" class="pa-2">
            <v-row>
              <v-col>
                <h4 class="mb-5">画像</h4>
                <p>
                  <input
                    type="file"
                    @change="load_image"
                    accept="image/gif, image/bmp, image/jpeg, image/png"
                    multiple
                  />
                </p>
              </v-col>
            </v-row>
            <v-row>
              <v-col v-for="(uploadFile, index) in data2.imageUrl" :key="index">
                <img
                  :src="uploadFile"
                  v-if="uploadFile != null"
                  alt="tmp"
                  style="max-width: 300px; border: solid 1px black"
                />
                <v-btn
                  class="mx-2"
                  fab
                  small
                  depressed
                  @click="deletePreview(index)"
                >
                  <v-icon> mdi-minus </v-icon>
                </v-btn>
              </v-col>
            </v-row>
            <v-row>
              <v-col>
                <h4 class="mb-5">ファイル</h4>
                <p>
                  <input
                    type="file"
                    @change="onFileSelected"
                    accept=".pdf"
                    multiple
                  />
                </p>
              </v-col>
            </v-row>
            <v-row v-if="fileUrls.fileUrl">
              <v-col
                v-for="(fileUrl, index) in fileUrls.fileUrl"
                :key="index"
                cols="12"
                ><v-icon>mdi-file-pdf-box</v-icon>
                <a :href="fileUrl" target="_blank">{{
                  fileNames.filename[index]
                }}</a>
              </v-col>
            </v-row>
          </v-sheet>
        </v-col>
      </v-row>
    </v-container>
  </v-form>
</template>

<script lang="ts">
import { reactive, defineComponent, ref } from "@vue/composition-api";
import pdfjsLib from "pdfjs-dist/webpack";

type Data2 = {
  imageUrl: string[];
};

type fileUrlData = {
  fileUrl: string[];
};

type fileNameData = {
  filename: string[];
};

const get_data_url = async (file: File): Promise<string> => {
  return new Promise((resolve, reject) => {
    const reader = new FileReader();
    reader.addEventListener("load", () => {
      const result = reader.result;
      if (typeof result === "string") {
        resolve(result);
      } else {
        reject(new Error("not string"));
      }
    });
    reader.readAsDataURL(file);
  });
};

export default defineComponent({
  name: "FileUpload",
  setup() {
    const data2 = reactive<Data2>({
      imageUrl: [],
    });

    const fileUrls = reactive<fileUrlData>({
      fileUrl: [],
    });

    const fileNames = reactive<fileNameData>({
      filename: [],
    });

    const load_image = async (event: Event) => {
      const selectedFile = event.target;

      if (!(selectedFile instanceof HTMLInputElement)) return;
      if (selectedFile.files == null || selectedFile.files.length == 0) {
        data2.imageUrl = [];
        return;
      }

      for (let i = 0; i < selectedFile.files.length; i++) {
        try {
          const result = await get_data_url(selectedFile.files[i]);
          data2.imageUrl.push(result);
        } catch (e) {
          alert(`ERROR: ${e}`);
        }
      }
      selectedFile.value = "";
    };

    const deletePreview = (index: number): void => {
      data2.imageUrl.splice(index, 1);
    };

    const pdfSrc = ref("");
    const fileName = ref("");

    const onFileSelected = async (event: Event) => {
      const selectedFile = event.target;
      if (!(selectedFile instanceof HTMLInputElement)) return;
      if (selectedFile.files == null || selectedFile.files.length == 0) {
        return;
      }

      //fileName.value = selectedFile.files[0].name;
      //pdfSrc.value = URL.createObjectURL(selectedFile.files[0]);

      for (let i = 0; i < selectedFile.files.length; i++) {
        try {
          fileUrls.fileUrl.push(URL.createObjectURL(selectedFile.files[i]));
          fileNames.filename.push(selectedFile.files[i].name);
        } catch (e) {
          alert(`ERROR: ${e}`);
        }
      }
      selectedFile.value = "";
    };

    return {
      load_image,
      data2,
      fileUrls,
      fileNames,
      deletePreview,
      pdfSrc,
      fileName,
      onFileSelected,
    };
  },
});
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>

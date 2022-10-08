<template>
  <v-form v-model="valid" ref="form">
    <v-container>
      <v-row>
        <v-col cols="12">
          <v-sheet color="white" elevation="1" class="pa-2">
            <v-row text-xs-center wrap>
              <v-col xs12>
                <h4 class="mb-5">画像</h4>
                <p>
                  <input
                    type="file"
                    @change="load_image"
                    accept="image/gif, image/bmp, image/jpeg, image/png"
                    multiple
                  />
                </p>
                <p>
                  <img
                    :src="data.imageUrl"
                    v-if="data.imageUrl != null"
                    alt="tmp"
                    style="max-width: 300px"
                  />
                </p>
              </v-col>
            </v-row>
          </v-sheet>
        </v-col>
      </v-row>
    </v-container>
  </v-form>
</template>

<script lang="ts">
import { reactive, defineComponent } from "@vue/composition-api";

type Data = {
  imageUrl?: string | undefined | null;
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
    const data = reactive<Data>({ imageUrl: null });

    const load_image = async (event: Event) => {
      const elm = event.target;
      if (!(elm instanceof HTMLInputElement)) return;
      if (elm.files == null || elm.files.length == 0) {
        data.imageUrl = null;
        return;
      }
      const file = elm.files[0];
      try {
        const result = await get_data_url(file);
        data.imageUrl = result;
      } catch (e) {
        alert(`ERROR: ${e}`);
      }
    };

    return {
      data,
      load_image,
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

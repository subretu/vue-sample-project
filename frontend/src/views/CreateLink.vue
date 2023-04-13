<template>
  <v-form>
    <v-container>
      <v-row>
        <v-col cols="12">
          <v-sheet color="white" elevation="1" class="pa-2">
            <v-row>
              <v-col xl="12" cols="12">
                <h3 class="mb-2" align="left">タイトル</h3>
                <v-text-field
                  label="入力してください。"
                  outlined
                  dense
                  class="input-text"
                  v-model="state.inputtext1"
                ></v-text-field>
              </v-col>
            </v-row>
            <v-row>
              <v-col xl="12" cols="12">
                <h3 class="mb-2" align="left">URL</h3>
                <v-text-field
                  label="入力してください。"
                  outlined
                  dense
                  class="input-text"
                  v-model="state.inputtext2"
                ></v-text-field>
              </v-col>
            </v-row>
            <v-row>
              <v-col>
                <v-btn depressed color="info" @click="createLink">作成</v-btn>
              </v-col>
            </v-row>
            <v-row>
              <v-col v-for="(value, index) in data.url" :key="index">
                <a
                  :href="value[1]"
                  :src="value[1]"
                  v-if="value != null"
                  alt="tmp"
                  >{{ value[0] }}</a
                >
              </v-col>
            </v-row>
          </v-sheet>
        </v-col>
      </v-row>
    </v-container>
  </v-form>
</template>

<script lang="ts">
import { defineComponent, reactive } from "@vue/composition-api";

type Data = {
  url: string[][];
};

export default defineComponent({
  name: "CreateLink",
  setup() {
    const data = reactive<Data>({
      url: [["vuetify", "https://v2.vuetifyjs.com/ja/api/v-text-field/#sass"]],
    });

    const state = reactive({
      inputtext1: "",
      inputtext2: "",
    });

    const createLink = (): void => {
      data.url.push([state.inputtext1, state.inputtext2]);
    };
    return {
      data,
      state,
      createLink,
    };
  },
});
</script>
<style scoped>
.input-text {
  width: 700px;
}
</style>

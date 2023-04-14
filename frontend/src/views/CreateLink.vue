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
            <v-row
              v-for="(value, key, index) in data.link"
              :key="index"
              class="ml-2 mb-1"
            >
              <a :href="value" :src="value" v-if="value != null">{{ key }}</a>
            </v-row>
          </v-sheet>
        </v-col>
      </v-row>
    </v-container>
  </v-form>
</template>

<script lang="ts">
import { defineComponent, reactive } from "@vue/composition-api";

export default defineComponent({
  name: "CreateLink",
  setup() {
    const data = reactive({
      link: {
        vuetify: "https://v2.vuetifyjs.com/ja/api/v-text-field/#sass",
        vuetify2: "https://v2.vuetifyjs.com/ja/api/v-text-field/#sass",
      } as Record<string, string>,
    });

    const state = reactive({
      inputtext1: "",
      inputtext2: "",
    });

    const createLink = () => {
      const newLink = {
        ...data.link,
        [state.inputtext1]: state.inputtext2,
      };
      data.link = newLink;
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

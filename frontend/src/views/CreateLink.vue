<template>
  <v-form>
    <v-container>
      <v-row>
        <v-col cols="12">
          <v-sheet color="white" elevation="1" class="pa-2">
            <v-row>
              <v-col xl="12" cols="5">
                <h3 class="mb-2" align="left">タイトル</h3>
                <v-text-field
                  label="入力してください。"
                  outlined
                  dense
                  class="input-text"
                  v-model="state.inputtext1"
                ></v-text-field>
              </v-col>
              <v-col xl="12" cols="5">
                <h3 class="mb-2" align="left">URL</h3>
                <v-text-field
                  label="入力してください。"
                  outlined
                  dense
                  class="input-text"
                  v-model="state.inputtext2"
                ></v-text-field>
              </v-col>
              <v-col class="mt-9" cols="1">
                <v-btn depressed color="info" @click="createLink">作成</v-btn>
              </v-col>
            </v-row>
            <v-row
              v-for="(value, key, index) in data.link"
              :key="index"
              class="ml-2 mb-1"
            >
              <a
                :href="value"
                :src="value"
                v-if="value != null"
                target="_blank"
                rel="noopener noreferrer"
                >{{ key }}</a
              >
            </v-row>
          </v-sheet>
        </v-col>
      </v-row>
    </v-container>
  </v-form>
</template>

<script lang="ts">
import { defineComponent, reactive, ref } from "@vue/composition-api";
import SampleApiService from "../services/SampleApiService";

export default defineComponent({
  name: "CreateLink",
  setup() {
    interface Data {
      link: { [key: string]: string } | undefined;
    }

    const data = reactive<Data>({
      link: {},
    });

    const state = reactive({
      inputtext1: "",
      inputtext2: "",
    });

    const response = ref(null);

    const getData = async () => {
      // get_json APIの実行
      try {
        await SampleApiService.get_json();
        const res = await SampleApiService.get_json();
        response.value = res.data;
        data.link = response.value?.[0][0];
      } catch (err) {
        console.log(err);
      }
    };

    const createLink = () => {
      const newLink = {
        ...data.link,
        [state.inputtext1]: state.inputtext2,
      };
      data.link = newLink;

      state.inputtext1 = "";
      state.inputtext2 = "";
    };

    // APIからデータを取得
    getData();

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

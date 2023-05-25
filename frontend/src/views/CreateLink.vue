<template>
  <v-form>
    <v-container>
      <v-row>
        <v-col cols="12">
          <v-sheet color="white" elevation="1" class="pa-2">
            <v-row>
              <v-col cols="1" align="left">
                <v-btn depressed color="info" @click="createLink"
                  >リンク作成</v-btn
                >
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
      <v-dialog v-model="show" width="auto">
        <v-card>
          <v-card-title />
          <v-row>
            <v-col>
              <h3 class="mb-2 ml-3" align="left">タイトル</h3>
              <v-text-field
                label="入力してください。"
                outlined
                dense
                class="input-text ml-3 mr-3"
                v-model="state.inputtext1"
              ></v-text-field>
            </v-col>
          </v-row>
          <v-row>
            <v-col>
              <h3 class="mb-2 ml-3" align="left">URL</h3>
              <v-text-field
                label="入力してください。"
                outlined
                dense
                class="input-text ml-3 mr-3"
                v-model="state.inputtext2"
              ></v-text-field>
            </v-col>
          </v-row>
          <v-card-actions>
            <v-btn color="info" depressed align="right" @click="createLink"
              >作成</v-btn
            >
          </v-card-actions>
        </v-card>
      </v-dialog>
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

    const show = ref(false);

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
      show.value = true;
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
      show,
      createLink,
    };
  },
});
</script>
<style scoped>
.input-text {
  width: 800px;
}
</style>

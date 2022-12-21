<template>
  <v-form>
    <v-container>
      <v-alert type="success" dismissible :value="isAlert"
        >Insert Sucessed</v-alert
      >
      <v-row>
        <v-col cols="12">
          <v-sheet color="white" elevation="1" class="pa-2">
            <v-row>
              <v-col xl="12" cols="12">
                <h3 class="mb-2" align="left">ID</h3>
                <v-text-field
                  label="入力してください。"
                  outlined
                  dense
                  class="input-text"
                  counter="50"
                  v-model="state.inputtext1"
                ></v-text-field>
              </v-col>
            </v-row>
            <v-divider class="mb-7"></v-divider>
            <v-row>
              <v-col xl="12" cols="12">
                <h3 class="mb-2" align="left">日付</h3>
                <v-text-field
                  label="入力してください。"
                  outlined
                  dense
                  class="input-text"
                  counter="50"
                  v-model="state.inputtext2"
                ></v-text-field>
              </v-col>
            </v-row>
            <v-divider class="mb-7"></v-divider>
            <v-row>
              <v-col xl="12" cols="12">
                <h3 class="mb-2" align="left">値</h3>
                <v-text-field
                  label="入力してください。"
                  outlined
                  dense
                  class="input-text"
                  counter="50"
                  v-model="state.inputtext3"
                ></v-text-field>
              </v-col>
            </v-row>
            <v-row>
              <v-col>
                <v-btn depressed color="info" @click="clickSample">登録</v-btn>
              </v-col>
            </v-row>
          </v-sheet>
        </v-col>
      </v-row>
    </v-container>
  </v-form>
</template>

<script lang="ts">
import { defineComponent, reactive, ref, watch } from "@vue/composition-api";
import SampleApiService from "@/services/SampleApiService";

export default defineComponent({
  name: "InputText",
  setup() {
    const state = reactive({
      inputtext1: null,
      inputtext2: null,
      inputtext3: null,
    });

    const isAlert = ref(false);

    watch(isAlert, () => {
      setTimeout(() => {
        isAlert.value = true;
      }, 5000);
    });

    const clickSample = async () => {
      // insert APIの実行
      try {
        await SampleApiService.insert({
          id: state.inputtext1,
          opsdate: state.inputtext2,
          value: state.inputtext3,
        });
        console.log("postok");
        isAlert.value = true;
      } catch (error) {
        console.log("error");
      }
    };

    return {
      isAlert,
      state,
      clickSample,
    };
  },
});
</script>
<style>
.input-text {
  width: 700px;
}
</style>

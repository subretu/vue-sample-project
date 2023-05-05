<template>
  <v-form>
    <v-container>
      <v-row>
        <v-col cols="12">
          <v-sheet color="white" elevation="1" class="pa-2">
            <v-row>
              <v-col cols="5">
                <h3 class="mb-2" align="left">Member ID</h3>
                <v-text-field
                  label="入力してください。"
                  outlined
                  dense
                  class="input-text"
                  v-model="state.inputtext1"
                  :rules="[requiredValidation, limitLengthValidation]"
                ></v-text-field>
              </v-col>
              <v-col cols="5">
                <h3 class="mb-2" align="left">Member Name</h3>
                <v-text-field
                  outlined
                  dense
                  class="input-text"
                  v-model="state.inputtext2"
                ></v-text-field>
              </v-col>
              <v-col cols="1" class="mt-9" align="left">
                <v-btn
                  depressed
                  color="info"
                  :disabled="!mytext"
                  @click="getMemberName(state.inputtext1)"
                  >DB連携</v-btn
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
import { defineComponent, reactive, computed } from "@vue/composition-api";
import SampleApiService from "../services/SampleApiService";

export default defineComponent({
  name: "CreateLink",
  setup() {
    const state = reactive<{
      inputtext1: string;
      inputtext2: string;
    }>({
      inputtext1: "",
      inputtext2: "",
    });

    // バリデーション関数
    const requiredValidation = (value: any) =>
      !!value || "必ず入力してください";

    const limitLengthValidation = (value: any) =>
      !isNaN(value) || "半角数字を入力してください";

    const getMemberName = async (inputText: string) => {
      try {
        const res = await SampleApiService.get_member_name(inputText);
        state.inputtext2 = res.data?.[0];
      } catch (err: any) {
        console.log(JSON.parse(err.request.response).detail);
        state.inputtext2 = "登録されていないIDです。";
      }
    };

    // バリデーションを通過すればボタンをクリック可能
    const mytext = computed(() => {
      return (
        requiredValidation(state.inputtext1) === true &&
        limitLengthValidation(state.inputtext1) === true
      );
    });

    return {
      state,
      mytext,
      requiredValidation,
      limitLengthValidation,
      getMemberName,
    };
  },
});
</script>
<style scoped>
.input-text {
  width: 700px;
}
</style>

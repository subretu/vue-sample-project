<template>
  <v-container>
    <v-row>
      <v-col cols="12">
        <v-sheet color="white" elevation="1" class="pa-2">
          <h3 class="mb-2" align="left">Member ID</h3>
          <v-row
            v-for="(input, index) in state.inputs"
            :key="index"
            class="mb-n8"
          >
            <v-col cols="5">
              <v-text-field
                label="入力してください。"
                outlined
                dense
                class="input-text"
                v-model="input.text1"
                @input="changeReadyButton(index)"
                :rules="[limitLengthValidation]"
              >
                <template v-slot:append>
                  <v-btn
                    depressed
                    dense
                    height="40"
                    width="120"
                    :class="[
                      state.dbConnectionStatus[index].success
                        ? 'connectionSuccess'
                        : state.dbConnectionStatus[index].fail
                        ? 'connectionFail'
                        : 'connectionDefault',
                    ]"
                    class="mr-n3 mt-n2"
                    @click="getMemberName(input.text1, index)"
                    :loading="state.linkings[index].linking"
                    :disabled="!mytext(index)"
                    >{{ state.buttonTexts[index] }}</v-btn
                  >
                </template></v-text-field
              >
            </v-col>
            <v-col cols="5">
              <v-text-field
                outlined
                dense
                class="input-text"
                v-model="input.text2"
              ></v-text-field>
            </v-col>
          </v-row>
          <v-btn fab depressed class="mt-6" @click="addInputForm()">
            <v-icon> mdi-plus-circle </v-icon>
          </v-btn>
        </v-sheet>
      </v-col>
    </v-row>
  </v-container>
</template>

<script lang="ts">
import { defineComponent, reactive } from "@vue/composition-api";
import SampleApiService from "../services/SampleApiService";

export default defineComponent({
  name: "CreateLink",
  setup() {
    const state = reactive<{
      inputs: { text1: string; text2: string }[];
      linkings: { linking: boolean }[];
      buttonTexts: string[];
      dbConnectionStatus: { success: boolean | null; fail: boolean | null }[];
    }>({
      inputs: [{ text1: "", text2: "" }],
      linkings: [{ linking: false }],
      buttonTexts: ["DB連携開始"],
      dbConnectionStatus: [{ success: null, fail: null }],
    });

    // バリデーション関数
    const limitLengthValidation = (value: any) =>
      !isNaN(value) || "半角数字を入力してください";

    const callGetMemberName = (inputText: string) => {
      return SampleApiService.get_member_name(inputText);
    };

    const getMemberName = (inputText: string, index: number) => {
      state.linkings[index].linking = true;
      const response = callGetMemberName(inputText);
      response
        .then((success) => {
          state.inputs[index].text2 = success.data?.[0];
          state.dbConnectionStatus[index].success = true;
          state.dbConnectionStatus[index].fail = false;
          state.buttonTexts[index] = "DB連携成功";
        })
        .catch((e) => {
          console.log(JSON.parse(e.request.response).detail);
          state.inputs[index].text2 = "";
          state.dbConnectionStatus[index].success = false;
          state.dbConnectionStatus[index].fail = true;
          state.buttonTexts[index] = "DB連携失敗";
        })
        .finally(() => {
          state.linkings[index].linking = false;
        });
    };

    // ボタンの表示を変更
    const changeReadyButton = (index: number) => {
      state.buttonTexts[index] = "DB連携開始";
      state.dbConnectionStatus[index].success = null;
      state.dbConnectionStatus[index].fail = null;
    };

    // 入力フォームを追加する
    const addInputForm = () => {
      state.inputs.push({ text1: "", text2: "" });
      state.linkings.push({ linking: false });
      state.dbConnectionStatus.push({ success: null, fail: null });
      state.buttonTexts.push("DB連携開始");
    };

    // バリデーションを通過かつ入力があればボタンをクリック可能
    const mytext = (index: number) => {
      return (
        limitLengthValidation(state.inputs[index].text1) === true &&
        state.inputs[index].text1 !== ""
      );
    };

    return {
      state,
      mytext,
      limitLengthValidation,
      getMemberName,
      changeReadyButton,
      addInputForm,
    };
  },
});
</script>
<style scoped>
.input-text {
  width: 700px;
}
.connectionDefault {
  background-color: rgba(255, 255, 255, 0.199) !important;
  border: 2px solid rgba(54, 34, 117, 0.6) !important;
  color: rgba(54, 34, 117);
  font-weight: normal;
}
.connectionSuccess {
  background-color: rgba(255, 255, 255, 0.199) !important;
  border-left: 1px solid rgb(128, 128, 128, 0.6) !important;
  color: red;
  font-weight: normal;
}
.connectionFail {
  background-color: rgba(255, 255, 255, 0.25) !important;
  border-left: 1px solid rgb(128, 128, 128, 0.6) !important;
  color: rgb(180, 170, 170);
  font-weight: normal;
}
</style>

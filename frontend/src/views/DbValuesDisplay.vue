<template>
  <v-container>
    <v-row>
      <v-col cols="12">
        <v-sheet color="white" elevation="1" class="pa-2">
          <h3 class="mb-2" align="left">Member ID</h3>
          <v-row v-for="(input, index) in state.inputs" :key="index">
            <v-col cols="5">
              <v-text-field
                label="入力してください。"
                outlined
                dense
                class="input-text"
                v-model="input.text1"
                @input="changeReadyButton(index)"
                :rules="[requiredValidation, limitLengthValidation]"
              >
                <template v-slot:append>
                  <v-btn
                    depressed
                    dense
                    height="40"
                    width="120"
                    :class="[
                      state.dbConnectionStatusSuccess
                        ? 'connectionSuccess'
                        : state.dbConnectionStatusFail
                        ? 'connectionFail'
                        : 'connectionDefault',
                    ]"
                    class="mr-n3 mt-n2"
                    @click="getMemberName(input.text1, index)"
                    :loading="state.linkings[index].linking"
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
          <v-btn fab depressed @click="addInputForm()">
            <v-icon> mdi-plus-circle </v-icon>
          </v-btn>
        </v-sheet>
      </v-col>
    </v-row>
  </v-container>
</template>

<script lang="ts">
import { defineComponent, ref, reactive, computed } from "@vue/composition-api";
import SampleApiService from "../services/SampleApiService";

export default defineComponent({
  name: "CreateLink",
  setup() {
    const state = reactive<{
      inputtext1: string;
      inputtext2: string;
      inputs: { text1: string; text2: string }[];
      linkings: [{ linking: boolean }];
      buttonTexts: string[];
      dbConnectionStatusSuccess: boolean | null;
      dbConnectionStatusFail: boolean | null;
    }>({
      inputtext1: "",
      inputtext2: "",
      inputs: [{ text1: "", text2: "" }],
      linkings: [{ linking: false }],
      buttonTexts: ["DB連携開始"],
      // 下記2ステータスもindexごとの用意が必要そう
      dbConnectionStatusSuccess: null,
      dbConnectionStatusFail: null,
    });

    // バリデーション関数
    const requiredValidation = (value: any) =>
      !!value || "必ず入力してください";
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
          state.inputs[0].text2 = success.data?.[0];
          state.dbConnectionStatusSuccess = true;
          state.dbConnectionStatusFail = false;
          state.buttonTexts[index] = "DB連携成功";
        })
        .catch((e) => {
          console.log(JSON.parse(e.request.response).detail);
          state.inputs[0].text2 = "";
          state.dbConnectionStatusSuccess = false;
          state.dbConnectionStatusFail = true;
          state.buttonTexts[index] = "DB連携失敗";
        })
        .finally(() => {
          state.linkings[index].linking = false;
        });
    };

    const changeReadyButton = (index: number) => {
      state.buttonTexts[index] = "DB連携開始";
      state.dbConnectionStatusSuccess = null;
      state.dbConnectionStatusFail = null;
    };

    // バリデーションを通過すればボタンをクリック可能
    const mytext = computed(() => {
      return (
        requiredValidation(state.inputtext1) === true &&
        limitLengthValidation(state.inputtext1) === true
      );
    });

    const addInputForm = () => {
      state.inputs.push({ text1: "", text2: "" });
      state.linkings.push({ linking: false });
      state.buttonTexts.push("DB連携開始");
    };

    return {
      state,
      mytext,
      requiredValidation,
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

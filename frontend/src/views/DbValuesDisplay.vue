<template>
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
                @input="changeReadyButton"
                :rules="[requiredValidation, limitLengthValidation]"
              >
                <template v-slot:append>
                  <v-btn
                    depressed
                    dense
                    height="40"
                    width="120"
                    color="info"
                    class="mr-n3 mt-n2"
                    :disabled="!mytext"
                    @click="getMemberName(state.inputtext1)"
                    :loading="linking"
                    >{{ buttonText }}</v-btn
                  >
                </template></v-text-field
              >
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
          </v-row>
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
    }>({
      inputtext1: "",
      inputtext2: "",
    });

    const linking = ref(false);

    const buttonText = ref("DB連携開始");

    // バリデーション関数
    const requiredValidation = (value: any) =>
      !!value || "必ず入力してください";

    const limitLengthValidation = (value: any) =>
      !isNaN(value) || "半角数字を入力してください";

    const getMemberName = async (inputText: string) => {
      try {
        linking.value = true;
        const res = await SampleApiService.get_member_name(inputText);
        state.inputtext2 = res.data?.[0];
        buttonText.value = "DB連携成功";
      } catch (err: any) {
        console.log(JSON.parse(err.request.response).detail);
        state.inputtext2 = "登録されていないIDです。";
        buttonText.value = "DB連携失敗";
      } finally {
        linking.value = false;
      }
    };

    const changeReadyButton = () => {
      buttonText.value = "DB連携開始";
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
      linking,
      buttonText,
      requiredValidation,
      limitLengthValidation,
      getMemberName,
      changeReadyButton,
    };
  },
});
</script>
<style scoped>
.input-text {
  width: 700px;
}
</style>

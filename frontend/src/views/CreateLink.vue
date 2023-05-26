<template>
  <v-form>
    <v-container>
      <v-row>
        <v-col cols="12">
          <v-sheet color="white" elevation="1" class="pa-2">
            <v-row>
              <v-col cols="1" align="left">
                <v-btn depressed color="info" @click="openStatus.value = true"
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
      <LinkInputDialog
        :openStatus="openStatus.value"
        @OpenStatusRequest="updateDialogStatusHandler"
        @input1="handleInput"
        @input2="handleInput2"
        @parentFunction="parentFunction"
      ></LinkInputDialog>
    </v-container>
  </v-form>
</template>

<script lang="ts">
import { defineComponent, reactive, ref } from "@vue/composition-api";
import SampleApiService from "../services/SampleApiService";
import LinkInputDialog from "../components/LinkInputDialog.vue";

export default defineComponent({
  name: "CreateLink",

  components: { LinkInputDialog },

  setup() {
    interface Data {
      link: { [key: string]: string } | undefined;
    }

    const data = reactive<Data>({
      link: {},
    });

    const state2 = reactive({
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
        [state2.inputtext1]: state2.inputtext2,
      };
      data.link = newLink;

      state2.inputtext1 = "";
      state2.inputtext2 = "";
    };

    const state3 = reactive({
      inputtext1: "",
      inputtext2: "",
    });

    const handleInput = (inputValue: string) => {
      state3.inputtext1 = inputValue;
    };

    const handleInput2 = (inputValue: string) => {
      state3.inputtext2 = inputValue;
    };

    const parentFunction = () => {
      openStatus.value = false;

      const newLink = {
        ...data.link,
        [state3.inputtext1]: state3.inputtext2,
      };
      data.link = newLink;

      state2.inputtext1 = "";
      state2.inputtext2 = "";
    };

    //const openStatus = ref(false);
    const openStatus = reactive<{
      value: boolean | undefined;
    }>({ value: false });

    const updateDialogStatusHandler = (status: boolean): void => {
      openStatus.value = status;
    };

    // APIからデータを取得
    getData();

    return {
      data,
      state2,
      openStatus,
      updateDialogStatusHandler,
      state3,
      handleInput,
      handleInput2,
      createLink,
      parentFunction,
    };
  },
});
</script>
<style scoped>
.input-text {
  width: 800px;
}
</style>

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
              class="ml-2 mb-1"
              v-for="linkItem in filteredLinks"
              :key="linkItem.key"
            >
              <a
                :key="linkItem.key"
                :href="linkItem.value"
                :src="linkItem.value"
                target="_blank"
                rel="noopener noreferrer"
              >
                {{ linkItem.key }}
              </a>
            </v-row>
          </v-sheet>
        </v-col>
      </v-row>
      <LinkInputDialog
        :openStatus="openStatus.value"
        @OpenStatusRequest="updateDialogStatusHandler"
        @input="handleInput"
        @displayLink="displayLink"
      ></LinkInputDialog>
      <v-overlay :value="state.isLoading">
        <v-progress-circular indeterminate size="64" />
      </v-overlay>
    </v-container>
  </v-form>
</template>

<script lang="ts">
import { defineComponent, reactive, ref, computed } from "@vue/composition-api";
import SampleApiService from "../services/SampleApiService";
import LinkInputDialog from "../components/LinkInputDialog.vue";

export default defineComponent({
  name: "CreateLink",

  components: { LinkInputDialog },

  setup() {
    interface LinkObject {
      [key: string]: string | undefined;
    }

    const data = ref<LinkObject[]>([]);

    const response = ref(null);

    const state = reactive({
      inputtext1: "",
      inputtext2: "",
      isLoading: false,
    });

    const getData = async () => {
      state.isLoading = true;
      // get_json APIの実行
      try {
        SampleApiService.get_json();
        const res = await SampleApiService.get_json();
        response.value = res.data;
        if (response.value?.[0][0] !== undefined) {
          data.value.push(response.value?.[0][0]);
          state.isLoading = false;
        }
      } catch (err) {
        console.log(err);
      }
    };

    const handleInput = (inputObject: { [key: string]: string }) => {
      state.inputtext1 = inputObject.inputtext1;
      state.inputtext2 = inputObject.inputtext2;
    };

    const displayLink = () => {
      openStatus.value = false;
      data.value.push({ [state.inputtext1]: state.inputtext2 });
    };

    const openStatus = reactive<{
      value: boolean | undefined;
    }>({ value: false });

    const updateDialogStatusHandler = (status: boolean): void => {
      openStatus.value = status;
    };

    const filteredLinks = computed(() => {
      return data.value
        .map((linkItem) => {
          const key = Object.keys(linkItem)[0];
          const value = linkItem[key];
          return { key, value };
        })
        .filter((linkItem) => linkItem.value !== undefined);
    });

    // APIからデータを取得
    getData();

    return {
      data,
      openStatus,
      updateDialogStatusHandler,
      state,
      handleInput,
      displayLink,
      filteredLinks,
    };
  },
});
</script>
<style scoped>
.input-text {
  width: 800px;
}
</style>

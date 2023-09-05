<template>
  <v-container>
    <v-row>
      <v-col cols="10">
        <v-sheet color="white" elevation="1">
          <div>
            <v-data-table
              :headers="headers"
              :items="viewData"
              hide-default-footer
              class="elevation-1"
            >
            </v-data-table>
          </div>
        </v-sheet>
      </v-col>
    </v-row>
  </v-container>
</template>

<script lang="ts">
import SampleApiService from "../services/SampleApiService";
import {
  defineComponent,
  reactive,
  computed,
  onMounted,
} from "@vue/composition-api";

type DataList = {
  id?: string | null;
  label?: string | null;
  data?: string | null;
};

type ApiResponse = { data: DataList[] };

export default defineComponent({
  setup() {
    const headers = [
      {
        text: "ID",
        value: "id",
      },
      {
        text: "名前",
        value: "label",
      },
      {
        text: "年齢",
        value: "data",
      },
    ];

    const getDay = async () => {
      const response = await SampleApiService.get();
      return response.data;
    };

    const apiResponse = reactive<ApiResponse>({ data: [] });

    const viewData = computed(() => {
      return apiResponse.data;
    });

    const displayData = async () => {
      const data = await getDay();
      apiResponse.data = data;
    };

    onMounted(async () => {
      await displayData();
    });

    return {
      headers,
      viewData,
    };
  },
});
</script>
<style>
.flex {
  display: flex;
}
.flex div {
  box-sizing: border-box;
}
.right {
  margin-right: auto;
}
.left {
  margin-left: auto;
}
.title {
  font-size: 18px;
}
</style>

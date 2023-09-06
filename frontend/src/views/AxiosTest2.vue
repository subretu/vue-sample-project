<template>
  <v-container>
    <v-dialog v-model="dialog" width="500">
      <v-card>
        <v-card-title class="headline">データ詳細</v-card-title>
        <v-card-text>
          <v-row>
            <v-col cols="3">ID</v-col
            ><v-col cols="9">{{ dialogData.id }}</v-col></v-row
          >
          <v-divider />
          <v-row>
            <v-col cols="3">日付</v-col
            ><v-col cols="9">{{ dialogData.label }}</v-col></v-row
          ><v-divider />
          <v-row>
            <v-col cols="3">合計値</v-col
            ><v-col cols="9">{{ dialogData.data }}</v-col></v-row
          >
        </v-card-text>
        <v-card-actions class="pa-6">
          <v-spacer />
          <v-btn @click="closeDialog">Close Dialog</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
    <v-row>
      <v-col cols="10">
        <v-sheet color="white" elevation="1">
          <v-data-table
            :headers="headers"
            :items="viewData"
            hide-default-footer
            class="elevation-1"
          >
            <template v-slot:[`item.id`]="{ item }">
              <td @click="openDialog(item)" class="link td-cell">
                <span>{{ item.id }}</span>
              </td>
            </template>
          </v-data-table>
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
  ref,
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
        text: "日付",
        value: "label",
      },
      {
        text: "合計値",
        value: "data",
      },
    ];

    const dialog = ref(false);

    const dialogData = reactive({
      id: "",
      label: "",
      data: 0,
    });

    const openDialog = (item: any) => {
      dialogData.id = item.id;
      dialogData.label = item.label;
      dialogData.data = item.data;
      dialog.value = true;
    };

    const closeDialog = (): void => {
      dialog.value = false;
    };

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
      dialog,
      dialogData,
      openDialog,
      closeDialog,
      viewData,
    };
  },
});
</script>
<style scoped>
.link {
  cursor: pointer;
}

.link:hover span {
  text-decoration: underline;
  color: blue;
}

.td-cell {
  font-family: Roboto, sans-serif;
  font-size: 14px;
}
</style>

<template>
  <v-container>
    <v-dialog v-model="dialog" width="500">
      <v-card>
        <v-card-title class="headline"
          >データ詳細
          <v-tooltip bottom>
            <template v-slot:activator="{ on, attrs }">
              <v-icon class="ml-1" color="black" dark v-bind="attrs" v-on="on">
                mdi-help-circle-outline
              </v-icon>
            </template>
            <span>これは選択されたデータの詳細を表示している画面です</span>
          </v-tooltip></v-card-title
        >
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
    <v-dialog v-model="dialog2" width="500">
      <v-card>
        <v-card-title class="headline"
          >データ詳細
          <v-tooltip bottom>
            <template v-slot:activator="{ on, attrs }">
              <v-icon class="ml-1" color="black" dark v-bind="attrs" v-on="on">
                mdi-help-circle-outline
              </v-icon>
            </template>
            <span>これは選択されたデータの詳細を表示している画面です</span>
          </v-tooltip></v-card-title
        >
        <v-row>
          <v-select
            v-model="selectedValue"
            :items="viewSelectBoxData"
            outlined
            dense
            class="ml-6 select-box"
          ></v-select>
          <v-btn class="ml-3" @click="applySelectData">apply</v-btn>
        </v-row>
        <v-card-text>
          <v-row>
            <v-col cols="3">ID</v-col
            ><v-col cols="9">{{ dialogData2.id }}</v-col></v-row
          >
          <v-divider />
          <v-row>
            <v-col cols="3">日付</v-col
            ><v-col cols="9">{{ dialogData2.label }}</v-col></v-row
          ><v-divider />
          <v-row>
            <v-col cols="3">合計値</v-col
            ><v-col cols="9">{{ dialogData2.data }}</v-col></v-row
          >
        </v-card-text>
        <v-card-actions class="pa-6">
          <v-spacer />
          <v-btn @click="closeDialog2">Close Dialog</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
    <v-dialog v-model="dialog3" width="500">
      <v-card>
        <v-card-title class="headline"
          >データ詳細
          <v-tooltip bottom>
            <template v-slot:activator="{ on, attrs }">
              <v-icon class="ml-1" color="black" dark v-bind="attrs" v-on="on">
                mdi-help-circle-outline
              </v-icon>
            </template>
            <span>これは選択されたデータの詳細を表示している画面です</span>
          </v-tooltip></v-card-title
        >
        <v-row>
          <v-select
            :items="viewSelectBoxData"
            outlined
            dense
            class="ml-6 select-box"
            @change="getTargetData"
            v-model="selectedValue"
          ></v-select>
        </v-row>
        <v-card-text v-if="selectedValue">
          <v-row>
            <v-col cols="3">ID</v-col
            ><v-col cols="9">{{ dialogData3.id }}</v-col></v-row
          >
          <v-divider />
          <v-row>
            <v-col cols="3">日付</v-col
            ><v-col cols="9">{{ dialogData3.label }}</v-col></v-row
          ><v-divider />
          <v-row>
            <v-col cols="3">合計値</v-col
            ><v-col cols="9">{{ dialogData3.data }}</v-col></v-row
          >
        </v-card-text>
        <v-card-actions class="pa-6">
          <v-spacer />
          <v-btn @click="closeDialog3">Close Dialog</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
    <v-row>
      <v-col cols="10"
        ><v-btn class="mb-2" @click="openDialog2">モーダル</v-btn>
        <v-btn class="mb-2 ml-2" @click="openDialog3">モーダル2</v-btn>
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
  watch,
} from "@vue/composition-api";

type DataList = {
  id?: string | null | undefined;
  label?: string | null | undefined;
  data?: number | null | undefined;
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

    const viewSelectBoxData = ref<string[]>([]);

    const selectBoxData = async () => {
      const data = await getDay();
      viewSelectBoxData.value.push("");
      for (const elem of data) {
        viewSelectBoxData.value.push(
          elem.id + "_" + elem.label + "_" + elem.data
        );
      }
    };

    const selectedValue = ref("");

    const dialog2 = ref(false);

    const dialogData2: DataList = reactive({
      id: "",
      label: "",
      data: 0,
    });

    const openDialog2 = () => {
      dialog2.value = true;
    };

    const closeDialog2 = (): void => {
      dialog2.value = false;
    };

    const applySelectData = () => {
      if (selectedValue.value === "") {
        dialogData2.id = "";
        dialogData2.label = "";
        dialogData2.data = 0;
        return;
      } else {
        const eventList = selectedValue.value.split("_");
        apiResponse.data.forEach(function (element) {
          if (element.id === eventList[0]) {
            dialogData2.id = element.id;
            dialogData2.label = element.label;
            dialogData2.data = element.data;
            return;
          }
        });
      }
    };

    const dialog3 = ref(false);

    const dialogData3: DataList = reactive({
      id: "",
      label: "",
      data: 0,
    });

    const openDialog3 = () => {
      dialog3.value = true;
    };

    const closeDialog3 = (): void => {
      dialog3.value = false;
    };

    const getTargetData = (event: any) => {
      if (event === "") {
        dialogData3.id = "";
        dialogData3.label = "";
        dialogData3.data = 0;
      }
      const eventList = event.split("_");
      apiResponse.data.forEach(function (element) {
        if (element.id === eventList[0]) {
          dialogData3.id = element.id;
          dialogData3.label = element.label;
          dialogData3.data = element.data;
          return;
        }
      });
    };

    // モーダルの開閉を監視
    watch(
      () => dialog.value,
      async () => {
        if (!dialog.value) {
          dialogData.id = "";
          dialogData.label = "";
          dialogData.data = 0;
        }
      }
    );

    watch(
      () => dialog2.value,
      async () => {
        if (dialog2.value) {
          await selectBoxData();
        } else {
          dialogData2.id = "";
          dialogData2.label = "";
          dialogData2.data = 0;
          viewSelectBoxData.value = [];
          selectedValue.value = "";
        }
      }
    );

    watch(
      () => dialog3.value,
      async () => {
        if (dialog3.value) {
          await selectBoxData();
        } else {
          dialogData3.id = "";
          dialogData3.label = "";
          dialogData3.data = 0;
          viewSelectBoxData.value = [];
          selectedValue.value = "";
        }
      }
    );

    onMounted(async () => {
      await displayData();
    });

    return {
      headers,
      dialog,
      dialog2,
      dialog3,
      dialogData,
      dialogData2,
      dialogData3,
      openDialog,
      openDialog2,
      openDialog3,
      applySelectData,
      getTargetData,
      closeDialog,
      closeDialog2,
      closeDialog3,
      selectedValue,
      viewData,
      viewSelectBoxData,
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
.v-select {
  width: 60%;
}
.select-box {
  max-width: 60%;
}
</style>

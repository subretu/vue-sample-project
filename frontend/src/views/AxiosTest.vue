<template>
  <v-container>
    <v-alert type="success" dismissible :value="isAlert">Deleted</v-alert>
    <h3>AAxiosTest</h3>
    <v-row>
      <v-col cols="10">
        <v-sheet color="white" elevation="1">
          <v-data-table :headers="headers" :items="items">
            <template v-slot:[`item.actions`]="{ item }">
              <v-icon class="mr-2" @click="editItem(item)"> mdi-pencil </v-icon>
              <v-icon @click="onClickDelete(item)"> mdi-delete </v-icon>
            </template>
          </v-data-table>
        </v-sheet>
      </v-col>
    </v-row>
    <!-- 削除ダイアログ -->
    <v-dialog v-model="show" persistent max-width="290">
      <v-card>
        <v-card-title />
        <v-card-text class="black--text">
          「ID {{ selectData.id }}」を削除しますか？
        </v-card-text>
        <v-card-actions>
          <v-spacer />
          <v-btn color="grey" text :disabled="loading" @click="onClickClose"
            >キャンセル</v-btn
          >
          <v-btn color="red" text :loading="loading" @click="deleteData"
            >削除</v-btn
          >
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-container>
</template>

<script>
import SampleApiService from "@/services/SampleApiService";
export default {
  data() {
    return {
      headers: [
        { text: "ID", value: "id" },
        { text: "日付", value: "label" },
        { text: "値", value: "data" },
        { text: "操作", value: "actions" },
      ],
      items: [],
      // ダイアログの表示状態
      show: false,
      // ローディング状態
      loading: false,
      // 削除データ
      selectData: "",
      isAlert: false,
    };
  },
  mounted() {
    this.get_day().then((response) => {
      this.items = response.data;
    });
  },
  watch: {
    isAlert: function () {
      setTimeout(() => {
        this.isAlert = false;
      }, 5000);
    },
  },
  methods: {
    get_day() {
      return SampleApiService.get();
    },
    onClickClose() {
      this.show = false;
    },
    onClickDelete(item) {
      this.show = true;
      this.selectData = item;
    },
    deleteData() {
      //SampleApiService.delete(this.selectData.id);
      SampleApiService.delete(this.selectData.id).then(() => {
        this.show = false;
        this.get_day().then((response) => {
          this.items = response.data;
        });
        this.isAlert = true;
      });
    },
  },
};
</script>

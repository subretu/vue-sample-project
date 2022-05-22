<template>
  <v-container>
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
    <DeleteDialog ref="deleteDialog" />
  </v-container>
</template>

<script>
import SampleApiService from "@/services/SampleApiService";
import DeleteDialog from "../components/DeleteDialog.vue";
export default {
  components: {
    DeleteDialog,
  },
  data() {
    return {
      headers: [
        { text: "ID", value: "id" },
        { text: "日付", value: "label" },
        { text: "値", value: "data" },
        { text: "操作", value: "actions" },
      ],
      items: [],
    };
  },
  mounted() {
    this.get_day().then((response) => {
      this.items = response.data;
    });
  },
  watch: {
    items: function () {
      this.get_day().then((response) => {
        this.items = response.data;
      });
      console.log("ok");
    },
  methods: {
    get_day() {
      return SampleApiService.get();
    },
    /** 削除ボタンがクリックされたとき */
    onClickDelete(item) {
      this.$refs.deleteDialog.open(item);
    },
  },
};
</script>

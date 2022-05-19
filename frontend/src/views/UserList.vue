<template>
  <v-container>
    <h3>UserList</h3>
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
import DeleteDialog from "../components/DeleteDialog.vue";
export default {
  name: "UserList",
  components: {
    DeleteDialog,
  },
  data() {
    return {
      headers: [
        {
          text: "ID",
          value: "id",
        },
        {
          text: "名前",
          value: "name",
        },
        {
          text: "年齢",
          value: "age",
        },
        {
          text: "操作",
          value: "actions",
        },
      ],
      items: [
        {
          id: 1,
          name: "高田健志",
          age: 33,
        },
        {
          id: 2,
          name: "横山緑",
          age: 42,
        },
        {
          id: 3,
          name: "山田太郎",
          age: 10,
        },
        {
          id: 4,
          name: "山崎イチゴ",
          age: 12,
        },
        {
          id: 5,
          name: "山田ニゴ",
          age: 16,
        },
        {
          id: 6,
          name: "山本一之進",
          age: 12,
        },
      ],
    };
  },
  methods: {
    /** 削除ボタンがクリックされたとき */
    onClickDelete(item) {
      this.$refs.deleteDialog.open(item);
    },
  },
};
</script>

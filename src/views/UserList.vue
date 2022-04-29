<template>
  <v-container>
    <v-row>
      <v-col cols="10">
        <h3>UserList</h3>
        <v-data-table :headers="headers" :items="items"></v-data-table>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: "UserList",
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
        { text: "年齢", value: "age" },
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
};
</script>

<template>
  <v-container>
    <h3>UserList</h3>
    {{ items.length }}件
    <v-row>
      <v-col cols="10">
        <v-sheet color="white" elevation="1">
          <v-data-table :headers="headers" :items="checkNull()"> </v-data-table>
        </v-sheet>
      </v-col>
    </v-row>
  </v-container>
</template>

<script lang="ts">
import { defineComponent } from "@vue/composition-api";

export default defineComponent({
  setup() {
    const headers = [
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
    ];
    const items = [
      {
        id: null,
        name: null,
        age: null,
      },
    ];
    const checkNull = () => {
      // オブジェクトの値一覧を取得
      const valueArray = Object.values(items[0]);
      // 全てnullの場合は空listを返してdata-tableで表示されないようにする
      if (valueArray.every((num) => num == null)) {
        return [];
      }
      return items;
    };
    return {
      headers,
      items,
      checkNull,
    };
  },
});
</script>

<template>
  <v-container>
    <h3>UserList</h3>
    {{ items.length }}件
    <v-row>
      <v-col cols="10">
        <v-sheet color="white" elevation="1">
          <v-data-table :headers="headers" :items="displayData"> </v-data-table>
        </v-sheet>
      </v-col>
    </v-row>
  </v-container>
</template>

<script lang="ts">
import { defineComponent, reactive, computed } from "@vue/composition-api";

class UserList {
  id?: string | null;
  name?: string | null;
  age?: number | string | null;
}

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
    // 初期値のセットアップ
    const items = reactive(new UserList());
    const setData = () => {
      items.id = null;
      items.name = "name";
      items.age = 23;
    };
    // データのnullを変換して表示データを作成する
    const displayData = computed(() => {
      setData();
      convertData(items);
      return [items];
    });
    // 値がnullなら変換する
    const convertData = (items: UserList) => {
      if (items.id == null) {
        items.id = "NoData";
      }
    };
    return {
      headers,
      items,
      setData,
      displayData,
    };
  },
});
</script>

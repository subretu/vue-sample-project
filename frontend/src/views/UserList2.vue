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
  age?: string | null;
}

interface UserListIF {
  [key: string]: string | null;
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
    // 表示データを定義
    const items = reactive(new UserList());
    // 初期値のセットアップ
    const setData = () => {
      items.id = "123";
      items.name = "name";
      items.age = null;
    };
    setData();
    // データのnullを変換して表示データを作成する
    const displayData = computed(() => {
      const data: UserListIF = {};
      const entries = Object.entries(items);
      for (const [k, v] of entries) {
        const key: string = k;
        if (v == null) {
          data[key] = "NoData";
        } else {
          data[key] = v;
        }
      }
      return [data];
    });
    return {
      headers,
      items,
      setData,
      displayData,
    };
  },
});
</script>

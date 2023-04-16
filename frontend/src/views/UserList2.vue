<template>
  <v-container>
    <h3>UserList</h3>
    <v-dialog v-model="dialog" width="auto">
      <v-card>
        <v-card-text> test </v-card-text>
        <v-card-actions>
          <v-btn color="primary" block @click="closeDialog">Close Dialog</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
    <v-row>
      <v-col cols="10">
        <v-sheet color="white" elevation="1">
          <v-data-table :headers="headers" :items="displayData">
            <template v-slot:item="{ item }">
              <td @click="handleCellClick" class="link td-cell py-2 pl-3">
                <span>{{ item.id }}</span>
              </td>
              <td class="link td-cell py-2 pl-4">{{ item.name }}</td>
              <td class="link td-cell py-2 pl-4">{{ item.age }}</td>
            </template>
          </v-data-table>
        </v-sheet>
      </v-col>
    </v-row>
  </v-container>
</template>

<script lang="ts">
import { defineComponent, reactive, computed, ref } from "@vue/composition-api";

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
      items.age = "123";
    };

    const handleCellClick = () => {
      dialog.value = true;
    };

    const dialog = ref(false);

    const closeDialog = (): void => {
      dialog.value = false;
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
      handleCellClick,
      setData,
      displayData,
      dialog,
      closeDialog,
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

<template>
  <v-container>
    <h3>UserList</h3>
    <v-dialog v-model="dialog" width="auto">
      <v-card>
        <v-card-text> {{ dialogData }} </v-card-text>
        <v-card-actions>
          <v-btn color="primary" block @click="closeDialog">Close Dialog</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
    <v-row>
      <v-col cols="10">
        <v-sheet color="white" elevation="1">
          <v-data-table
            :headers="headers"
            :items="displayData"
            class="elevation-0"
          >
            <template v-slot:[`item.id`]="{ item }">
              <td @click="handleCellClick(item)" class="link td-cell">
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
      items.name = "kenji";
      items.age = "123";
    };

    const dialogData = ref("");

    const handleCellClick = (item: any) => {
      console.log(item);
      dialogData.value = item.name;
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
      dialogData,
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

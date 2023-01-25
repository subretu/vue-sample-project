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
        id: "fff",
        name: "fff",
        age: "fff",
      },
    ];
    const checkNull = () => {
      const id = items[0].id;
      const name = items[0].name;
      const age = items[0].age;

      // 1つでもNULLだったら返さないようにする
      if (id == null || name == null || age == null) {
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

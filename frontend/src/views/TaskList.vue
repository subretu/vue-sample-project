<template>
  <v-container>
    <v-row>
      <v-col cols="10">
        <v-sheet color="white" elevation="1">
          <h3>TaskList</h3>
          <v-data-table :headers="headers" :items="items"></v-data-table>
        </v-sheet>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: "TaskList",
  data() {
    return {
      headers: [
        {
          text: "ID",
          value: "id",
        },
        {
          text: "タスク",
          value: "task",
        },
        {
          text: "期限日",
          value: "limitdate",
        },
      ],
      items: [
        {
          id: 1,
          task: "メルカリを出す",
          limitdate: "2022-05-01",
        },
        {
          id: 2,
          task: "牛乳を消費する",
          limitdate: "2022-05-03",
        },
        {
          id: 3,
          task: "ファミマでクーポンを使う",
          limitdate: "2022-05-10",
        },
      ],
    };
  },
};
</script>

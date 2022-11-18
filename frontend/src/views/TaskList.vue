<!-- eslint-disable vue/require-v-for-key -->
<template>
  <v-container class="pa-3" fluid>
    <v-card class="translucent" tile>
      <h3 class="pa-4">TASKLIST</h3>
      <v-row class="ma-0">
        <v-col class="pa-4" cols="4">
          <h3>table A</h3>
          <table border="1" style="border-collapse: collapse">
            <tbody align="center">
              <tr>
                <th>ID</th>
                <td v-for="item in items">
                  最大：{{ item.id }}、最小：{{ item.id2 }}、平均：{{
                    item.id3
                  }}
                </td>
              </tr>
              <tr>
                <th>Task</th>
                <td v-for="item in items">{{ item.task }}</td>
              </tr>
              <tr>
                <th>LimitD</th>
                <td v-for="item in items">{{ item.limitdate }}</td>
              </tr>
            </tbody>
          </table>
        </v-col>
        <v-col class="pa-4" cols="4">
          <h3>table A</h3>
          <table border="1" style="border-collapse: collapse">
            <tbody align="center">
              <tr>
                <th>ID</th>
                <td v-for="item in items" width="150">{{ item.id }}</td>
              </tr>
              <tr>
                <th>Task</th>
                <td v-for="item in items">{{ item.task }}</td>
              </tr>
              <tr>
                <th>LimitD</th>
                <td v-for="item in items">{{ item.limitdate }}</td>
              </tr>
            </tbody>
          </table>
        </v-col>
        <v-col class="pa-4" cols="4">
          <h3>table A</h3>
          <table border="1" style="border-collapse: collapse">
            <tbody align="center">
              <tr>
                <th>ID</th>
                <td v-for="item in items">{{ item.id }}</td>
              </tr>
              <tr>
                <th>Task</th>
                <td v-for="item in items">{{ item.task }}</td>
              </tr>
              <tr>
                <th>LimitD</th>
                <td v-for="item in items">{{ item.limitdate }}</td>
              </tr>
            </tbody>
          </table>
        </v-col>
      </v-row>
    </v-card>
  </v-container>
</template>

<script>
export default {
  name: "TaskList",
  data() {
    return {
      items: [
        {
          id: 1,
          id2: 2,
          id3: 3,
          task: "メルカリを出す",
          limitdate: "2022-05-01",
        },
      ],
    };
  },
};
</script>
<style scoped>
table {
  display: contents;
  width: 100%;
  border: solid 1px #bbccce;
}
table tbody {
  width: 100%;
  display: table;
}
th {
  background-color: #bbccce64;
  font-weight: normal;
  width: 50%;
}
</style>

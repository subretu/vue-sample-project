<!-- eslint-disable vue/require-v-for-key -->
<template>
  <v-card class="translucent" tile>
    <h3 class="pa-4">TASKLIST</h3>
    <v-row class="ma-0">
      <v-col class="pa-4" cols="4">
        <h3>Table A</h3>
        <table border="1" style="border-collapse: collapse">
          <tbody align="center">
            <tr>
              <th>ID</th>
              <td v-for="item in viewdata[0]">
                最大：{{ item.id }}、最小：{{ item.id2 }}、平均：{{ item.id3 }}
              </td>
            </tr>
            <tr>
              <th>Task</th>
              <td v-for="item in viewdata[0]">{{ item.task }}</td>
            </tr>
            <tr>
              <th>LimitD</th>
              <td v-for="item in viewdata[0]">{{ item.limitdate }}</td>
            </tr>
          </tbody>
        </table>
      </v-col>
      <v-divider vertical class="mb-4"></v-divider>
      <v-col class="pa-4" cols="4">
        <h3>Table B</h3>
        <table border="1" style="border-collapse: collapse">
          <tbody align="center">
            <tr>
              <th>ID</th>
              <td v-for="item in viewdata[1]">{{ item.id }}</td>
            </tr>
            <tr>
              <th>Task</th>
              <td v-for="item in viewdata[1]">{{ item.task }}</td>
            </tr>
            <tr>
              <th>LimitD</th>
              <td v-for="item in viewdata[1]">{{ item.limitdate }}</td>
            </tr>
          </tbody>
        </table>
      </v-col>
      <v-divider vertical class="mb-4"></v-divider>
      <v-col class="pa-4" cols="4">
        <h3>Table C</h3>
        <table border="1" style="border-collapse: collapse">
          <tbody align="center">
            <tr>
              <th>ID</th>
              <td v-for="item in viewdata[2]">{{ item.id }}</td>
            </tr>
            <tr>
              <th>Task</th>
              <td v-for="item in viewdata[2]">{{ item.task1 }}</td>
            </tr>
            <tr>
              <th>Task</th>
              <td v-for="item in viewdata[2]">{{ item.task2 }}</td>
            </tr>
            <tr>
              <th>Task</th>
              <td v-for="item in viewdata[2]">{{ item.task3 }}</td>
            </tr>
            <tr>
              <th>LimitD</th>
              <td v-for="item in viewdata[2]">{{ item.limitdate }}</td>
            </tr>
          </tbody>
        </table>
      </v-col>
    </v-row>
  </v-card>
</template>

<script>
export default {
  props: {
    viewdata: {
      default: function () {
        return "";
      },
    },
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

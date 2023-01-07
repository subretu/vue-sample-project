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
              <td v-for="item in viewdata">{{ item.id }}</td>
            </tr>
            <tr>
              <th>Task</th>
              <td v-for="item in viewdata">{{ item.task }}</td>
            </tr>
            <tr>
              <th>LimitD</th>
              <td v-for="item in viewdata">{{ item.limitd }}</td>
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

<template>
  <v-container>
    <h3>ChartSample</h3>
    <v-row>
      <v-col cols="10">
        <line-chart></line-chart>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import LineChart from "../components/LineChart";
export default {
  components: { LineChart },
};
</script>

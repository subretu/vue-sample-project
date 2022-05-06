<template>
  <v-container>
    <h3>ChartSample</h3>
    <v-row>
      <v-col cols="10">
        <line-chart
          :chart-data="datacollection"
          :options="options"
        ></line-chart>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import LineChart from "../components/LineChart";

export default {
  components: {
    LineChart,
  },
  data() {
    return {
      datacollection: null,
      options: null,
    };
  },
  mounted() {
    this.fillData();
  },
  methods: {
    fillData() {
      (this.datacollection = {
        labels: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        datasets: [
          {
            label: "sample",
            borderColor: "#0000ff",
            data: [100, 90, 60, 70, 50, 30, 40, 50, 60, 100],
            fill: false,
          },
        ],
      }),
        (this.options = {
          responsive: true,
          maintainAspectRatio: false,
          title: {
            display: true,
            text: "Line chart",
          },
          legend: {
            display: true,
          },
        });
    },
  },
};
</script>

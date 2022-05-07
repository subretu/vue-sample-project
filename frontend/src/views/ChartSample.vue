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
import SampleApiService from "@/services/SampleApiService";

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
      let labelsList = [];
      let dataList = [];
      this.get_day().then((response) => {
        this.items = response.data;
        for (const elem of this.items) {
          labelsList.push(elem["label"]);
          dataList.push(elem["data"]);
        }
      });
      (this.datacollection = {
        labels: labelsList,
        datasets: [
          {
            label: "sample",
            borderColor: "#0000ff",
            data: dataList,
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
            display: false,
          },
        });
    },
    get_day() {
      return SampleApiService.get();
    },
  },
};
</script>

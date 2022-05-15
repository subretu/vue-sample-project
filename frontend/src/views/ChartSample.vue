<template>
  <v-container>
    <h3>ChartSample</h3>
    <v-row>
      <v-col cols="12" sm="12" md="6" lg="4">
        <line-chart :chart-data="datacollection" :options="options" />
      </v-col>
      <v-col cols="12" sm="12" md="6" lg="4">
        <line-chart :chart-data="datacollection" :options="options" />
      </v-col>
      <v-col cols="12" sm="12" md="6" lg="4">
        <bar-chart :chart-data="datacollection" :options="options" />
      </v-col>
      <v-col cols="12" sm="12" md="6" lg="4">
        <bar-chart :chart-data="datacollection" :options="options" />
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import LineChart from "../components/LineChart";
import BarChart from "../components/BarChart";
import SampleApiService from "@/services/SampleApiService";

export default {
  components: {
    LineChart,
    BarChart,
  },
  data() {
    return {
      datacollection: {},
      options: {},
    };
  },
  async mounted() {
    this.fillData();
  },
  methods: {
    get_day() {
      return SampleApiService.get();
    },
    fillData() {
      let labelsList = [];
      let dataList = [];
      this.get_day().then((response) => {
        this.items = response.data;
        for (const elem of this.items) {
          labelsList.push(elem["label"]);
          dataList.push(elem["data"]);
        }
        this.datacollection = {
          labels: labelsList,
          datasets: [
            {
              label: "sample",
              borderColor: "#0000ff",
              data: dataList,
              fill: false,
            },
          ],
        };
        this.options = {
          responsive: true,
          maintainAspectRatio: false,
          title: {
            display: true,
            text: "Line chart",
          },
          legend: {
            display: true,
          },
        };
      });
    },
  },
};
</script>

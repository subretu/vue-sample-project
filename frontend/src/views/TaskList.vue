<template>
  <v-container class="pa-3" fluid>
    <div v-show="(nowYear, nowMonth)">
      <p class="text-h5">
        <strong>{{ nowYear }}年{{ nowMonth }}月</strong>
      </p>
    </div>
    <SummaryTable :viewdata="[items, items2, items3]" />
  </v-container>
</template>

<script>
import SummaryTable from "../components/SummaryTable.vue";

export default {
  name: "TaskList",
  components: {
    SummaryTable,
  },
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
      items2: [
        {
          id: 59,
          task: "牛乳を買う",
          limitdate: "2022-05-25",
        },
      ],
      items3: [
        {
          id: 100,
          task1: "ポケモン赤を買う",
          task2: "ポケモン緑を買う",
          task3: "ポケモン青を買う",
          limitdate: "2022-10-25",
        },
      ],
      nowYear: "",
      nowMonth: "",
    };
  },
  methods: {
    getYear: function () {
      var date = new Date();
      return date.getFullYear();
    },
    getMonth: function () {
      var date = new Date();
      return ("0" + (date.getMonth() + 1)).slice(-2);
    },
  },
  mounted: function () {
    this.nowYear = this.getYear();
    this.nowMonth = this.getMonth();
  },
};
</script>

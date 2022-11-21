<template>
  <v-container class="pa-3" fluid>
    <div v-show="(nowYear, nowMonth)">
      <p class="text-h5">
        <strong>{{ nowYear }}年{{ nowMonth }}月</strong
        ><v-btn @click="tableaChange">値変更</v-btn>
      </p>
    </div>
    <SummaryTable :viewdata="[taskData, items2, items3]" />
  </v-container>
</template>

<script>
import SummaryTable from "../components/SummaryTable.vue";
import SampleApiService from "@/services/SampleApiService";

export default {
  name: "TaskList",
  components: {
    SummaryTable,
  },
  data() {
    return {
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
      taskData: [],
      is_first: "1",
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
    get_task() {
      return SampleApiService.task(this.is_first);
    },
    fillData() {
      this.get_task(this.is_first).then((response) => {
        this.taskData = response.data;
      });
    },
    tableaChange() {
      console.log("okk");
      this.is_first = "2";
      this.fillData(this.is_first);
    },
  },
  async mounted() {
    this.nowYear = this.getYear();
    this.nowMonth = this.getMonth();
    this.fillData(this.is_first);
  },
};
</script>

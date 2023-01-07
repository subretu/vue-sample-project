<template>
  <v-container class="pa-3" fluid>
    <div v-show="(displayDate.nowYear, displayDate.nowMonth)" align="left">
      <p class="text-h5">
        <strong>{{ displayDate.nowYear }}年{{ displayDate.nowMonth }}月</strong>
      </p>
    </div>
    <SummaryTable :viewdata="state.taskData" />
  </v-container>
</template>

<script lang="ts">
import { defineComponent, reactive, onMounted } from "@vue/composition-api";
import SummaryTable from "../components/SummaryTable2.vue";
import SampleApiService from "../services/SampleApiService";

export default defineComponent({
  name: "TaskList2",
  components: {
    SummaryTable,
  },
  setup() {
    const displayDate = reactive({
      nowYear: "",
      nowMonth: "",
    });
    const state = reactive({
      taskData: [],
    });
    const is_first = 1;

    const getYear = (): void => {
      var date = new Date();
      displayDate.nowYear = String(date.getFullYear());
    };

    const getMonth = (): void => {
      var date = new Date();
      displayDate.nowMonth = String(("0" + (date.getMonth() + 1)).slice(-2));
    };

    const get_task = (is_first: number) => {
      return SampleApiService.task(is_first);
    };

    const fillData = (is_first: number): void => {
      get_task(is_first).then((response) => {
        state.taskData = response.data;
      });
    };

    onMounted(() => {
      getYear;
      getMonth;
      fillData(is_first);
    });

    return {
      displayDate,
      state,
    };
  },
});
</script>

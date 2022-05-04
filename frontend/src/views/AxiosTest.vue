<template>
  <v-container>
    <h3>AAxiosTest</h3>
    <v-row>
      <v-col cols="10">
        <v-sheet color="white" elevation="1">
          <v-data-table :headers="headers" :items="items"></v-data-table>
        </v-sheet>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import SampleApiService from "@/services/SampleApiService";

export default {
  components: {},
  data() {
    return {
      headers: [
        { text: "日付", value: "label" },
        { text: "値", value: "data" },
      ],
      items: [],
    };
  },
  mounted() {
    this.get_day().then((response) => {
      this.items = response.data;
    });
  },
  methods: {
    get_day() {
      return SampleApiService.get();
    },
  },
};
</script>

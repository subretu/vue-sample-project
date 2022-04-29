<template>
  <div class="hello">
    <h1>{{ message }}</h1>
  </div>
</template>

<script>
import SampleApiService from "@/services/SampleApiService";

export default {
  components: {},
  data() {
    return {
      message: "",
    };
  },
  mounted() {
    this.get_day().then((response) => {
      this.message = response.data.label;
    });
  },
  methods: {
    get_day() {
      return SampleApiService.get();
    },
  },
};
</script>

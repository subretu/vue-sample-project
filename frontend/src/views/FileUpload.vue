<template>
  <v-container>
    <input
      style="display: none"
      ref="input"
      type="file"
      accept="image/jpeg, image/jpg, image/png"
      @change="selectedFile()"
    />
    <v-layout text-xs-center wrap>
      <v-flex xs12>
        <!-- ファイルの選択 -->
        <div color="primary" @click="btnclick" class="drop_area">
          select image
        </div>
      </v-flex>
    </v-layout>
  </v-container>
</template>
<script>
export default {
  data() {
    return {
      // 略
    };
  },
  methods: {
    // selectfileボタン押下時
    btnclick() {
      this.$refs.input.click();
    },
    async selectedFile() {
      this.isUploading = true;

      const file = this.$refs.input.files[0];
      if (!file) {
        return;
      } // 以下ファイルの操作
    },
  },
};
</script>
<style>
.drop_area {
  color: gray;
  font-weight: bold;
  font-size: 1.2em;
  display: flex;
  justify-content: center;
  align-items: center;
  width: 500px;
  height: 250px;
  border: 5px solid gray;
  border-radius: 15px;
}
</style>

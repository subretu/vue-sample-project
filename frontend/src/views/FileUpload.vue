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
          画像を選択して下さい
          <v-icon class="my-2" alt="search icon" :x-large="true">
            mdi-plus
          </v-icon>
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
:root {
  --background-color: #ffffff;
  --background-color-hover: #b9b9b9;
  --border-color: #6d6d6d;
  --border-color-hover: #757575;
  --line-border: 2px;
  --text-color-dark: #505050;
}
.drop_area {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  max-width: 700px;
  min-height: 150px;
  border: 5px dashed var(--border-color);
  background-color: var(--background-color);
  color: var(--text-color-dark);
  border-radius: 20px;
  box-sizing: border-box;
  transition: background-color 160ms ease;
  font-weight: bold;
}
</style>

const { defineConfig } = require("@vue/cli-service");
module.exports = defineConfig({
  transpileDependencies: ["vuetify"],
  //CORSエラー対策
  devServer: {
    proxy: {
      "/day": {
        target: "http://localhost:8000",
      },
    },
  },
});

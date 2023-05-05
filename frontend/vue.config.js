const { defineConfig } = require("@vue/cli-service");
module.exports = defineConfig({
  transpileDependencies: ["vuetify"],
  //CORSエラー対策
  devServer: {
    proxy: {
      "/day": {
        target: "http://localhost:8000",
      },
      "/delete": {
        target: "http://localhost:8000",
      },
      "/insert": {
        target: "http://localhost:8000",
      },
      "/task": {
        target: "http://localhost:8000",
      },
      "/jsondata": {
        target: "http://localhost:8000",
      },
      "/get_member": {
        target: "http://localhost:8000",
      },
    },
  },
  publicPath: "./",
});

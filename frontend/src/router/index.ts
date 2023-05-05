import Vue from "vue";
import VueRouter, { RouteConfig } from "vue-router";
import HomeView from "../views/HomeView.vue";

Vue.use(VueRouter);

const routes: Array<RouteConfig> = [
  {
    path: "/",
    name: "home",
    component: HomeView,
  },
  {
    path: "/userlist",
    name: "userlist",
    component: () => import("../views/UserList.vue"),
  },
  {
    path: "/userlist2",
    name: "userlist2",
    component: () => import("../views/UserList2.vue"),
  },
  {
    path: "/tasklist",
    name: "tasklist",
    component: () => import("../views/TaskList.vue"),
  },
  {
    path: "/tasklist2",
    name: "tasklist2",
    component: () => import("../views/TaskList2.vue"),
  },
  {
    path: "/axiostest",
    name: "axiostest",
    component: () => import("../views/AxiosTest.vue"),
  },
  {
    path: "/chartsample",
    name: "chartsample",
    component: () => import("../views/ChartSample.vue"),
  },
  {
    path: "/fileupload",
    name: "fileupload",
    component: () => import("../views/FileUpload.vue"),
  },
  {
    path: "/fileupload2",
    name: "fileupload2",
    component: () => import("../views/FileUpload2.vue"),
  },
  {
    path: "/Inputtext",
    name: "Inputtext",
    component: () => import("../views/InputtText.vue"),
  },
  {
    path: "/createlink",
    name: "createlink",
    component: () => import("../views/CreateLink.vue"),
  },
  {
    path: "/dbvaluesdisplay",
    name: "dbvaluesdisplay",
    component: () => import("../views/DbValuesDisplay.vue"),
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;

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
    path: "/tasklist",
    name: "tasklist",
    component: () => import("../views/TaskList.vue"),
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
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;

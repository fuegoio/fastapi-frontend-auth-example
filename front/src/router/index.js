import { createRouter, createWebHistory } from "vue-router";
import Home from "../views/Home.vue";
import GithubCallback from "../views/GithubCallback.vue";

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home
  },
  {
    path: "/auth/github",
    name: "GithubCallback",
    component: GithubCallback
  }
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
});

export default router;

const Module = () => import("./Module.vue");
const Dashboard = () => import("./views/Dashboard.vue");

const moduleRoute = {
  path: "/user",
  component: Module,
  children: [
    {
      path: ":user",
      component: Dashboard
    },
  ]
};

export default router => {
  router.addRoute(moduleRoute);
};

const Module = () => import("./Module.vue");
const Dashboard = () => import("./views/Dashboard.vue");
const PasswordChange = () => import("./views/PasswordChange.vue");

const moduleRoute = {
  path: "/user",
  component: Module,
  children: [
    {
      name: "main",
      path: ":user/",
      component: Dashboard
    },
    {
      name: "passwordchange",
      path: "settings/passwordchange",
      component: PasswordChange
    },
  ]
};

export default router => {
  router.addRoute(moduleRoute);
};

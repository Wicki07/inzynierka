const Module = () => import("./Module.vue");
const Dashboard = () => import("./views/Dashboard.vue");
const PasswordChange = () => import("./views/PasswordChange.vue");
const PlacesList = () => import("./views/PlacesList.vue");

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
    {
      name: "passwordchange",
      path: "settings/manageposts",
      component: PlacesList
    },
  ]
};

export default router => {
  router.addRoute(moduleRoute);
};

const Module = () => import("./Module.vue");
const Dashboard = () => import("./views/Dashboard.vue");
const PasswordChange = () => import("./views/PasswordChange.vue");
const ManagePosts = () => import("./views/ManagePosts.vue");
const EditPlace = () => import("./views/EditPlace.vue");

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
      path: "settings/manageposts",
      component: ManagePosts
    },
    {
      name: "editplace",
      path: "settings/manageposts/:title?",
      props: true,
      component: EditPlace
    },
  ]
};

export default router => {
  router.addRoute(moduleRoute);
};

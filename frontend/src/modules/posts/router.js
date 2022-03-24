const Module = () => import("./Module.vue");
const AddPlace = () => import("./views/AddPlace.vue");

const moduleRoute = {
  path: "/posts",
  component: Module,
  children: [
    {
      path: "addplace",
      component: AddPlace
    },

  ]
};

export default router => {
  router.addRoute(moduleRoute);
};

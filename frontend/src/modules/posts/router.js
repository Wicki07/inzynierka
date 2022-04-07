const Module = () => import("./Module.vue");
const AddPlace = () => import("./views/AddPlace.vue");
const PlacesList = () => import("./views/PlacesList.vue");

const moduleRoute = {
  path: "/posts",
  component: Module,
  children: [
    {
      path: "addplace",
      component: AddPlace
    },
    {
      path: "list",
      component: PlacesList
    },

  ]
};

export default router => {
  router.addRoute(moduleRoute);
};

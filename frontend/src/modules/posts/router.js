const Module = () => import("./Module.vue");
const AddPlace = () => import("./views/AddPlace.vue");
const StateChoose = () => import("./views/StateChoose.vue");
const PlacesList = () => import("./views/PlacesList.vue");
const PlaceView = () => import("./views/PlaceView.vue");

const moduleRoute = {
  path: "/posts",
  component: Module,
  children: [
    {
      path: "addplace",
      component: AddPlace
    },
    {
      path: "state",
      component: StateChoose
    },
    {
      path: "list/:state?",
      props: true,
      component: PlacesList
    },
    {
      path: "list",
      props: true,
      component: PlacesList
    },
    {
      name: 'place',
      path: "place/:title?",
      props: true,
      component: PlaceView
    },
  ]
};

export default router => {
  router.addRoute(moduleRoute);
};

const Module = () => import("./Module.vue");
const Login = () => import("./views/Login.vue");
const Register = () => import("./views/Register.vue");
const Activate = () => import("./views/Activate.vue");

const moduleRoute = {
  path: "/auth",
  component: Module,
  children: [
    {
      path: "login",
      component: Login
    },
    {
      path: "register",
      component: Register
    },
    {
      path: "activate/:code",
      component: Activate,
    },

  ]
};

export default router => {
  router.addRoute(moduleRoute);
};

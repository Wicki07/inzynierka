import axios from "axios";

const baseURL = process.env.VUE_APP_BACKEND_URL;
const axiosAPI = axios.create({
  baseURL: baseURL, // Adres do serwera Django
  timeout: 5000,
  headers: {
    Authorization: localStorage.getItem("token")
      ? "Token " + localStorage.getItem("token")
      : null,
    "Content-Type": "application/json",
    accept: "application/json",
  },
});

axiosAPI.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem("token");
    if (token) {
      config.headers["Authorization"] = "Token " + token;
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

axiosAPI.interceptors.response.use(
  (response) => {
    return response;
  },
  async function (error) {
    const originalRequest = error.config;

    if (
      originalRequest.url === baseURL + "/api/auth/logout" &&
      error.response.status === 401 &&
      error.response.statusText === "Unauthorized"
    ) {
      axiosAPI.defaults.headers["Authorization"] =
        "Token " + localStorage.getItem("token");
      originalRequest.headers["Authorization"] =
        "Token " + localStorage.getItem("token");

      return axiosAPI;
    }

    return Promise.reject(error);
  }
);

export { axiosAPI };

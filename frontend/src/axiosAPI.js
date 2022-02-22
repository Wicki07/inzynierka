import axios from "axios";

const baseURL = "http://127.0.0.1:8000";
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

axiosAPI.interceptors.response.use(
  (response) => {
    return response;
  },
  async function (error) {
    const originalRequest = error.config;
    if (typeof error.response === "undefined") {
      alert(
        "A server/network error occurred. " +
          "Looks like CORS might be the problem. " +
          "Sorry about this - we will get it fixed shortly."
      );
      return Promise.reject(error);
    }

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

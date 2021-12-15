export default {
    state: () => ({
        username: "",
        email: "",
        isAuthenticated: false
    }),
    getters: {

    },
    mutations: {
        setUser(state, user) {
            state.username = user.username
            state.email = user.email
            state.isAuthenticated = true
        },
        resetUser(state) {
            state.username = ""
            state.email = ""
            state.isAuthenticated = false
        }
    },
    actions: {
        setUser({ commit }, user) {
            commit("setUser", user);
        },
        resetUser({ commit }) {
            commit("resetUser")
        }
    },
}
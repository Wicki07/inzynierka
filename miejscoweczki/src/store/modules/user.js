export default {
    state: () => ({
        username: "",
        email: ""
    }),
    getters: {

    },
    mutations: {
        setUser(state, user) {
            state.username = user.username
            state.email = user.email
        },
        resetUser(state) {
            state.username = ""
            state.email = ""
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
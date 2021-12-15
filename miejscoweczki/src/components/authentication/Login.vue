<template>
    <v-container>
        <v-card>
            <v-text-field
                class="mt-5"
                v-model="username"
                label="username"
            ></v-text-field>
            <v-text-field
                class="mt-5"
                v-model="password"
                label="hasło"
                type="password"
            ></v-text-field>
            <v-btn
                color="succes"
                @click="login"
            >Zaloguj
            </v-btn>
        </v-card>
    </v-container>
</template>
<script>
import axios from 'axios'
import { mapActions } from "vuex"
export default {
    data(){
        return {
            username: "",
            password: "",
        }
    },
    methods: {
        ...mapActions(["setUser", "resetUser"]),
        login(){
            axios.post("http://127.0.0.1:8000/api/auth/login",{
                username: this.username,
                password: this.password
            }).then(res => {
                localStorage.setItem('token', res.data.token);
                this.setUser(res.data.user)
            }).catch(err => {
                console.log("err")
                console.log(err)
            })
        },
    }
}
</script>
<style scoped>

</style>
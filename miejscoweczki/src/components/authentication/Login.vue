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
            <v-btn
                color="succes"
                @click="logout"
            >Wyloguj
            </v-btn>
        </v-card>
    </v-container>
</template>
<script>
import {axiosAPI} from '../../axiosAPI';
import { mapActions } from "vuex"
export default {
    data(){
        return {
            username: "",
            password: "",
        }
    },
    methods: {
        ...mapActions(["setUser"]),
        login(){
            axiosAPI.post("http://127.0.0.1:8000/api/auth/login",{
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
        logout(){
            axiosAPI.get("http://127.0.0.1:8000/api/auth/logout").then(res => {
                console.log(res.data)
            }).catch(err => {
                console.log("err")
                console.log(err)
            })
        }
    }
}
</script>
<style scoped>

</style>
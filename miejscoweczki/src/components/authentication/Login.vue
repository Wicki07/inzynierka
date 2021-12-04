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
            >Zaloguj
            </v-btn>
        </v-card>
    </v-container>
</template>
<script>
import axios from 'axios'
export default {
    data(){
        return {
            username: "",
            password: "",
            token: "",
        }
    },
    methods: {
        login(){
            axios.post("http://127.0.0.1:8000/api/auth/login",{
                username: this.username,
                password: this.password
            }).then(res => {
                localStorage.setItem('token', res.data.token);
                this.token = res.data.token
            }).catch(err => {
                console.log("err")
                console.log(err)
            })
        },
        logout(){
            let config = {
                headers: {
                    "Content-Type": "application/json"
                }
            }
            config.headers["Authorization"] = `Token ${this.token}`
            axios.get("http://127.0.0.1:8000/api/auth/logout", config).then(res => {
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
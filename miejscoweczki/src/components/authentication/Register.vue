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
                v-model="email"
                label="email"
            ></v-text-field>
            <v-text-field
                class="mt-5"
                v-model="password"
                label="hasło"
                type="password"
            ></v-text-field>
            <v-text-field
                class="mt-5"
                v-model="password2"
                label="powtórz hasło"
                type="password"
            ></v-text-field>
            <v-btn
                color="succes"
                @click="register"
            >Zarejestruj
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
            email: "",
            password: "",
            password2: "",
        }
    },
    methods: {
        ...mapActions(["setUser"]),
        register(){
            axios.post("http://127.0.0.1:8000/api/auth/register",{
                username: this.username,
                email: this.email,
                password: this.password
            }).then(res => {
                localStorage.setItem('token', res.data.token);
                this.setUser(res.data.user)
            }).catch(res => {
                console.log(res)
            })
        }
    }
}
</script>
<style scoped>

</style>
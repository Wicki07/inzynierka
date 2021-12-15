
import axios from 'axios';



const baseURL = 'http://127.0.0.1:8000'
const axiosAPI = axios.create({
    baseURL: baseURL,// Adres do serwera Django
    timeout: 5000,
    headers: {
        Authorization: localStorage.getItem('token')
            ? 'Token ' + localStorage.getItem('token')
            : null,
            'Content-Type': 'application/json',
            accept: 'application/json',
    },
})


export {axiosAPI}

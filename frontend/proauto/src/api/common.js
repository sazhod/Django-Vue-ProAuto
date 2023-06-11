import axios from 'axios'

const backendHost = 'sazhod.ru';
const apiUrl = `http://${backendHost}:8000/api/v1/`

console.log(apiUrl)
console.log('!!!message!!!')

export const HTTP = axios.create({
  baseURL: apiUrl
})
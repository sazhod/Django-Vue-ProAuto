import axios from 'axios'

const backendHost = '172.19.0.2';
const apiUrl = `http://${backendHost}:8000/api/v1/`

console.log(apiUrl)
console.log('!!!message!!!')

export const HTTP = axios.create({
  baseURL: apiUrl
})
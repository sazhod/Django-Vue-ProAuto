import axios from 'axios'

const backendHost = '212.113.117.97';
const apiUrl = `http://${backendHost}:8000/api/v1/`

console.log(apiUrl)
console.log('!!!message!!!')

export const HTTP = axios.create({
  baseURL: apiUrl
})
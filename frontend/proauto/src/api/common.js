import axios from 'axios'

const apiUrl = `http://sazhod.ru:8000/api/v1/`

console.log(apiUrl)

export const HTTP = axios.create({
  baseURL: apiUrl
})
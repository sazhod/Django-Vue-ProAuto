import axios from 'axios'

const backendHost = process.env.VUE_APP_BACKEND_HOST;
const apiUrl = `http://${backendHost}:8000/api/v1/`

export const HTTP = axios.create({
  baseURL: apiUrl
})
import axios from 'axios'
import { env } from './config'

export const gatewayApi = axios.create({
  //baseURL: `${env.REACT_APP_GATEWAY_API_HOST}:${env.REACT_APP_GATEWAY_API_PORT}/api/v1/`,
  baseURL: `${env.REACT_APP_GATEWAY_API_HOST}/api/v1/`,
  withCredentials:true
})

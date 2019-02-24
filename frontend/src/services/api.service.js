import axios from "axios";
import { API_URL } from "@/services/config";

const client = axios.create({
  baseURL: API_URL
})

const ApiService = {
  get(resource, slug = "") {
    return client({
      method: 'get',
      url: `${resource}/${slug}`
    }).then(response => {
      return response.data
    }).catch(error => {
      throw new Error(`ApiService ${error}`);
    })
  },
  post(resource, data) {
    return client({
      method: 'post',
      url: `${resource}/`,
      data
    }).then(response => {
      return response.status_code
    }).catch(error => {
      console.log(error)
      throw new Error(`ApiService ${error}`);
    })
  },
  delete(resource, slug = "") {
    return client({
      method: 'delete',
      url: `${resource}/${slug}`
    }).then(response => {
      return response
    }).catch(error => {
      throw new Error(`ApiService ${error}`)
    })
  }
};

export default ApiService;

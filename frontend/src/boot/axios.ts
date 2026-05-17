import { boot } from 'quasar/wrappers';
import axios from 'axios';
import type { AxiosInstance } from 'axios';

declare module '@vue/runtime-core' {
  interface ComponentCustomProperties {
    $axios: AxiosInstance;
    $api: AxiosInstance;
  }
}

// Базовый URL твоего Django-сервера
const api = axios.create({ baseURL: 'http://127.0.0.1:8000' });

export default boot(({ app }) => {
  app.config.globalProperties.$axios = axios;
  app.config.globalProperties.$api = api;
});

export { api };

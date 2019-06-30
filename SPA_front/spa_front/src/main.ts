import Vue from 'vue';
import App from './App.vue';
import router from './router';
import store from './store';
import axios, {AxiosInstance} from 'axios';


Vue.prototype.$axios = axios;


Vue.config.productionTip = false;

import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';

Vue.use(ElementUI);

declare module 'Vue/types/vue' {
    interface Vue {
        $axios: AxiosInstance;
    }
}

new Vue({
  router,
  store,
  render: (h) => h(App),
}).$mount('#app');



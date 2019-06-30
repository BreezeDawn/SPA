import Vue from 'vue';
import Router from 'vue-router';
import SubPage1 from './views/SubPage1.vue';

Vue.use(Router);

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
        name: 'sub_page1',
        component: SubPage1,
    },
    {
        path: '/sub_page2',
        name: 'sub_page2',
      // route level code-splitting
      // this generates a separate chunk (about.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
        component: () => import(/* webpackChunkName: "about" */ './views/SubPage2.vue'),
    },
  ],
});

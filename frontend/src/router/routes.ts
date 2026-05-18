const routes = [
  {
    path: '/',
    redirect: '/sir'
  },
  {
    path: '/sir',
    component: () => import('pages/SIRPage.vue'),
    meta: { title: 'SIR модель', index: 1 }
  },
  {
    path: '/sir2',
    component: () => import('pages/SIRPage2.vue'),
    meta: { title: 'SIR2 модель', index: 2 }
  },
  {
    path: '/sir3',
    component: () => import('pages/SIRPage.vue'),
    meta: { title: 'SIR3 модель', index: 3 }
  }
];

export default routes;

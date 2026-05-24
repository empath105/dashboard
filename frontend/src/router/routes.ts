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
    path: '/fkpp',
    component: () => import('pages/FKPPPage.vue'),
    meta: { title: 'Ф-КПП модель', index: 2 }
  },
  {
    path: '/turing',
    component: () => import('pages/TuringPage.vue'),
    meta: { title: 'Пятна Тьюринга', index: 3 }
  }
];

export default routes;

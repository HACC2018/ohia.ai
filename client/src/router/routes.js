const routes = [
  {
    path: '/',
    component: () => import('layouts/Layout.vue'),
    children: [
      {
        path: '',
        component: () => import('pages/Index.vue'),
      },
    ],
  },
  {
    path: '/help',
    component: () => import('layouts/Layout.vue'),
    children: [
      {
        path: '',
        component: () => import('pages/Help.vue'),
      },
    ],
  },
  {
    path: '/plant/:id',
    component: () => import('layouts/Layout.vue'),
    children: [
      {
        path: '',
        component: () => import('pages/PlantDetails.vue'),
      },
    ],
  },
  {
    path: '/identify',
    component: () => import('layouts/Layout.vue'),
    children: [
      {
        path: '',
        name: 'identify',
        component: () => import('pages/PlantIdentification.vue'),
        props: true,
      },
    ],
  },
];

// Always leave this as last one
if (process.env.MODE !== 'ssr') {
  routes.push({
    path: '*',
    component: () => import('pages/Error404.vue'),
  });
}

export default routes;

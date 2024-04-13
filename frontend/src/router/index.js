import { createRouter, createWebHistory } from '@ionic/vue-router';
import LoginPage from '../views/LoginPage.vue';
import SignupPage from '../views/SignupPage.vue';

const routes = [
  {
    path: '/',
    redirect: '/login'
  },
  {
    path: '/login',
    name: 'Login',
    component: LoginPage
  },
  {
    path: '/signup',
    name: 'Signup',
    component: SignupPage
  },
]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes
})

export default router

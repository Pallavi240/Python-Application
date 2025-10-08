import { createRouter, createWebHistory } from 'vue-router'
import Loginpage from '../pages/Loginpage.vue'
import SignupPage from '../pages/SignupPage.vue'

const routes = [
  { path: '/', redirect: '/login' },
  { path: '/login', component: Loginpage },
  { path: '/signup', component: SignupPage },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router

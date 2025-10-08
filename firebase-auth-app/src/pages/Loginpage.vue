<template>
  <div class="container">
    <div class="auth-card">
      <h1>Login</h1>

      <form @submit.prevent="loginUser">
        <input type="email" v-model="email" placeholder="Email" required />
        <input type="password" v-model="password" placeholder="Password" required />
        <button type="submit">Login</button>
      </form>

      <p class="toggle">
        Don’t have an account?
        <router-link to="/signup">Sign Up</router-link>
      </p>

      <p v-if="message" class="message">{{ message }}</p>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'

const email = ref('')
const password = ref('')
const message = ref('')

const backendURL = import.meta.env.VITE_API_URL // change to your Flask API

const loginUser = async () => {
  try {
    const res = await axios.post(`${backendURL}/login`, { email: email.value, password: password.value })
    message.value = 'Login Successful ✅'
    localStorage.setItem('token', res.data.token)
  } catch (err) {
    message.value = err.response?.data?.error || 'Invalid credentials ❌'
  }
}
</script>

<style scoped>
@import "../style.css";
</style>

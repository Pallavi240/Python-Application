<template>
  <div class="container">
    <div class="auth-card">
      <h1>Sign Up</h1>

      <form @submit.prevent="registerUser">
        <input type="email" v-model="email" placeholder="Email" required />
        <input type="password" v-model="password" placeholder="Password" required />
        <button type="submit">Create Account</button>
      </form>

      <p class="toggle">
        Already have an account?
        <router-link to="/login">Login</router-link>
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

const registerUser = async () => {
  try {
    const res = await axios.post(`${backendURL}/signup`, {
      email: email.value,
      password: password.value,
    })
    message.value = res.data.message || 'User created successfully ✅'
  } catch (err) {
    message.value = err.response?.data?.error || 'Email already exists ❌'
  }
}
</script>

<style scoped>
@import '../style.css';
</style>

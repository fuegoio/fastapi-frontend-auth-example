<template>
  <div class="home">
    <div @click="login">Login</div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Home",
  methods: {
    login() {
      axios.get("http://localhost:8000/auth/login").then(response => {
        window.location = response.data.url;
      });
    }
  }
};
</script>

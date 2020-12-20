<template>
  <div class="about">
    <div v-if="!user">Authorizing ...</div>
    <div v-else>
      {{ user }}
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "GithubCallback",
  data() {
    return {
      token: undefined,
      user: undefined
    };
  },
  created() {
    this.authorize();
  },
  methods: {
    authorize() {
      const data = {
        state: this.$route.query.state,
        code: this.$route.query.code
      };

      axios
        .post("http://localhost:8000/auth/authorize", data)
        .then(response => {
          this.token = response.data.access_token;
          this.getUser();
        })
        .catch(() => {
          this.$router.replace("/");
        });
    },
    getUser() {
      const headers = { Authorization: `Bearer ${this.token}` };
      axios
        .get("http://localhost:8000/auth/me", { headers: headers })
        .then(response => {
          this.user = response.data;
        });
    }
  }
};
</script>

<template>
  <md-card class="md-card-profile">
    <div class="md-card-avatar">
      <img class="img" :src="cardUserImage" />
    </div>

    <md-card-content>
      <h6 class="category text-gray">Full Stack Developer</h6>
      <h4 class="card-title">Milton Lenis</h4>
      <p class="card-description">
        Hi! thank you for taking your time to review my Hiring Project, I had so
        much fun developing it!
      </p>
      <p class="card-description left">
        Here you have some useful links:
      </p>
      <ul class="align-left">
        <li>
          <a href="https://github.com/MiltonLn/britecore_test_project"
            >This Project's Repo</a
          >
        </li>
        <li><a href="https://miltonlenis.com/">My Webpage</a></li>
        <li><a href="https://github.com/MiltonLn/">My GitHub Profile</a></li>
        <li>
          <a href="https://www.linkedin.com/notifications/"
            >My LinkedIn Profile</a
          >
        </li>
      </ul>
    </md-card-content>
  </md-card>
</template>
<script>
export default {
  name: "user-card",
  props: {
    cardUserImage: {
      type: String,
      default: require("@/assets/img/faces/milton.jpg")
    }
  },
  data() {
    return {};
  }
};
</script>
<style></style>

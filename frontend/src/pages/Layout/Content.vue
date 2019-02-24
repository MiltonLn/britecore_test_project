<template>
  <transition name="fade" mode="out-in">
    <div class="content">
      <div class="md-layout">
        <div class="md-layout-item md-medium-size-100 md-size-66">
          <router-view></router-view>
        </div>
        <div class="md-layout-item md-medium-size-100 md-size-33">
          <user-card></user-card>
        </div>
      </div>
    </div>
  </transition>
</template>
<script>
import { UserCard } from "@/pages";
export default {
  components: {
    UserCard
  }
};
</script>
<style>
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.1s;
}

.fade-enter,
    .fade-leave-to
      /* .fade-leave-active in <2.1.8 */

 {
  opacity: 0;
}
</style>

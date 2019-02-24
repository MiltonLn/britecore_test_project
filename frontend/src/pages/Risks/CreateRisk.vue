<template>
  <div class="content">
    <div class="md-layout">
      <div class="md-layout-item md-medium-size-100 md-size-100">
        <create-risk-form data-background-color="blue"> </create-risk-form>
      </div>
    </div>
  </div>
</template>

<script>
import { CreateRiskForm } from "@/components";

export default {
  components: {
    CreateRiskForm
  }
};
</script>

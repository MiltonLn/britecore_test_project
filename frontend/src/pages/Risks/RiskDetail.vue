<template>
  <div class="content">
    <div class="md-layout">
      <div class="md-layout-item">
        <md-card>
          <md-card-header data-background-color="blue">
            <h4 class="title">Risk Detail</h4>
          </md-card-header>
          <md-card-content>
            <div id="typography">
              <div class="title">
                <h3>{{ risk.risk_type_name }}</h3>
              </div>
              <div v-for="(value, name) in risk.field_values" :key="name" class="row">
                <div class="tim-typo">
                  <h5>
                    <span class="tim-note">{{ name }}</span>
                    {{ value }}
                  </h5>
                </div>
              </div>
            </div>
          </md-card-content>
        </md-card>
      </div>
    </div>
  </div>
</template>

<script>
import ApiService from "@/services/api.service";

export default {
  props: {
    dataBackgroundColor: {
      type: String,
      default: ""
    }
  },
  data() {
    return {
      risk: {}
    }
  },
  mounted() {
    this.fetchRisk();
  },
  methods: {
    async fetchRisk() {
      const response = await ApiService.get('risks', this.$route.params.id);
      this.risk = response;
    }
  }
};
</script>

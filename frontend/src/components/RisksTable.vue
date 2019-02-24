<template>
  <div>
    <md-table v-model="risks" :table-header-color="tableHeaderColor">
      <md-table-row slot="md-table-row" slot-scope="{ item }">
        <md-table-cell md-label="Type">{{ item.risk_type_name }}</md-table-cell>
        <md-table-cell md-label="Field Values">
          <span v-for="(value, name) in item.field_values" :key="name">
            <b>{{ name }}: </b> {{ value }},&nbsp;
          </span>
        </md-table-cell>
        <md-table-cell>
          <md-button @click="riskDetail(item.id)" class="md-just-icon md-simple md-info">
            <md-icon>pageview</md-icon>
            <md-tooltip md-direction="top">Detail</md-tooltip>
          </md-button>
          <md-button @click="deleteRisk(item.id)" class="md-just-icon md-simple md-danger">
            <md-icon>delete</md-icon>
            <md-tooltip md-direction="top">Delete</md-tooltip>
          </md-button>
        </md-table-cell>
      </md-table-row>
    </md-table>
  </div>
</template>

<script>
import ApiService from "@/services/api.service";

export default {
  name: "risks-table",
  props: {
    tableHeaderColor: {
      type: String,
      default: ""
    }
  },
  data() {
    return {
      risks: []
    };
  },
  mounted() {
    this.fetchRisks();
  },
  methods: {
    async fetchRisks() {
      const response = await ApiService.get("risks");
      this.risks = response;
    },
    async deleteRisk(riskId) {
      await ApiService.delete("risks", riskId)
      this.fetchRisks()
    },
    riskDetail(riskId) {
      this.$router.push(`/risks/${riskId}`)
    }
  }
};
</script>

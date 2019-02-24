<template>
  <form>
    <md-card>
      <md-card-header :data-background-color="dataBackgroundColor">
        <h4 class="title">Create Risk</h4>
        <p class="category">Please select a Risk Type and then fill the fields</p>
      </md-card-header>

      <md-card-content>
        <div class="md-layout">
          <div class="md-layout-item md-small-size-100 md-size-100">
            <md-field>
              <label for="movie">Risk Type</label>
              <md-select
                v-on:md-selected="selectRiskType"
                v-model="selectedRiskType"
                name="selectedRiskType"
                id="selectedRiskType"
              >
                <md-option v-for="type in riskTypes" :key="type.id" :value="type.id">{{ type.name }}</md-option>
              </md-select>
            </md-field>
          </div>
          <div
            class="md-layout-item md-small-size-100 md-size-50"
            v-for="(fieldType, fieldName) in formFields"
            :key="fieldName"
          >
            <md-field v-if="fieldType === 'STRING'">
              <label>{{ fieldName }}</label>
              <md-input v-model="formData[fieldName]" type="text"></md-input>
            </md-field>
            <md-field v-else-if="fieldType === 'NUMBER'">
              <label>{{ fieldName }}</label>
              <md-input v-model="formData[fieldName]" type="number"></md-input>
            </md-field>
            <md-datepicker
              v-model="formData[fieldName]"
              v-else-if="fieldType === 'DATE'"
              md-immediately
            >
              <label>{{ fieldName }}</label>
            </md-datepicker>
            <md-field v-else-if="Array.isArray(fieldType)">
              <label>{{ fieldName }}</label>
              <md-select
                v-model="formData[fieldName]"
                name="selectedRiskType"
                id="selectedRiskType"
              >
                <md-option v-for="option in fieldType" :key="option" :value="option">{{ option }}</md-option>
              </md-select>
            </md-field>
          </div>
          <span class="error-message" v-if="validationError" :style="{color: 'red'}">{{ validationError }}</span>
          <div class="md-layout-item md-size-100 text-right">
            <md-button v-on:click="submitForm" class="md-raised md-info">Save</md-button>
          </div>
        </div>
      </md-card-content>
    </md-card>
  </form>
</template>
<script>
import ApiService from "@/services/api.service";

export default {
  name: "create-risk-form",
  props: {
    dataBackgroundColor: {
      type: String,
      default: ""
    }
  },
  data() {
    return {
      riskTypes: [],
      selectedRiskType: "",
      formFields: {},
      formData: {},
      validationError: ""
    };
  },
  mounted() {
    this.fetchRiskTypes();
  },
  methods: {
    async fetchRiskTypes() {
      const response = await ApiService.get("risk-types");
      this.riskTypes = response;
    },
    createFormData(fields) {
      let data = {};
      for (let field of Object.keys(fields)) {
        data[field] = null;
      }
      return data;
    },
    selectRiskType() {
      if (this.selectedRiskType) {
        const riskType = this.riskTypes.find(
          type => type.id === this.selectedRiskType
        );
        this.validationError = "";
        this.formFields = riskType.fields_type;
        this.formData = this.createFormData(this.formFields);
      }
    },
    async submitForm() {
      if (this.selectedRiskType) {
        if (Object.values(this.formData).some(value => value === null)) {
          // If at least one field is not filled
          this.validationError = "Please fill all the fields"
          return
        }
        this.validationError = ""
        const data = {risk_type: this.selectedRiskType, field_values: this.formData}
        debugger
        await ApiService.post("risks", data)

        this.$router.push('/risks')
        return
      }
      this.validationError = "Please select the Risk Type";
    }
  }
};
</script>
<style></style>

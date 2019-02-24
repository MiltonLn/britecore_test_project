import DashboardLayout from "@/pages/Layout/DashboardLayout.vue";

import CreateRisk from "@/pages/Risks/CreateRisk.vue";
import RiskList from "@/pages/Risks/RiskList.vue";
import RiskDetail from "@/pages/Risks/RiskDetail.vue";

const routes = [
  {
    path: "/",
    component: DashboardLayout,
    redirect: "/create-risk",
    children: [
      {
        path: "create-risk",
        name: "Create Risk",
        component: CreateRisk
      },
      {
        path: "risks",
        name: "List Risks",
        component: RiskList
      },
      {
        path: "risks/:id",
        name: "Risk Detail",
        component: RiskDetail
      }
    ]
  }
];

export default routes;

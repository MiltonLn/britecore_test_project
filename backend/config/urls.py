from django.urls import path, include
from rest_framework import routers

from risk_types import views


router = routers.DefaultRouter()
router.register(r'risk-types', views.RiskTypeViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

from rest_framework import viewsets

from .serializers import RiskSerializer
from .models import Risk


class RiskViewSet(viewsets.ModelViewSet):
    """
    Simple ViewSet for viewing and editing Risks
    """
    queryset = Risk.objects.all()
    serializer_class = RiskSerializer
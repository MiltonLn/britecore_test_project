from rest_framework import viewsets

from .serializers import RiskTypeSerializer
from .models import RiskType


class RiskTypeViewSet(viewsets.ModelViewSet):
    """
    Simple ViewSet for viewing and editing Risk Types
    """
    queryset = RiskType.objects.all()
    serializer_class = RiskTypeSerializer
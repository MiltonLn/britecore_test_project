import uuid

from django.db import models
from django.contrib.postgres.fields import JSONField

from risk_types.models import RiskType


class Risk(models.Model):
    """Model to store an actual Risk with its field values"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    risk_type = models.ForeignKey(RiskType, on_delete=models.CASCADE)
    field_values = JSONField()
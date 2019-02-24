import uuid

from django.db import models
from django.contrib.postgres.fields import JSONField

from risk_types.models import RiskType


class Risk(models.Model):
    """Model to store an actual Risk with its field values"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    risk_type = models.ForeignKey(RiskType, on_delete=models.CASCADE)
    field_values = JSONField()

    @property
    def risk_type_name(self):
        return self.risk_type.name

    def __repr__(self):
        return f'{self.risk_type} ({field_values})'

    def __str__(self):
        return f'{self.risk_type} ({field_values})'

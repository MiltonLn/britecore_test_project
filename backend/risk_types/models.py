import uuid

from django.db import models
from django.contrib.postgres.fields import JSONField


class RiskType(models.Model):
    """Model to represent the Risk Type and its fields definition"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    fields_type = JSONField()

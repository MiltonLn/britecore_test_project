from rest_framework import serializers

from .constants import SupportedTypes
from .models import RiskType


class RiskTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RiskType
        fields = ['id', 'name', 'fields_type']

    def validate_fields_type(self, value):
        """Check that fields_type has the right format"""
        for field_name, field_type in value.items():
            if type(field_type) == SupportedTypes.ENUM:
                if not all(type(option) == str for option in field_type):
                    raise serializers.ValidationError(
                        f'"{field_name}" is not a strings list'
                    )
            elif field_type not in SupportedTypes.atomic_types():
                raise serializers.ValidationError(
                    f'Unsupported type "{field_type}" for field "{field_name}"'
                )
        return value
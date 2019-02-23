from rest_framework import serializers

from risk_types.constants import SupportedTypes
from .models import Risk


class RiskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Risk
        fields = ['id', 'risk_type', 'field_values']

    def has_correct_fields(self, fields, mandatory_fields):
        return set(fields) == set(mandatory_fields)

    def validate(self, data):
        """Validate that field_values has the right fields with the right types"""
        field_values = data['field_values']
        mandatory_fields = data['risk_type'].fields_type

        if not self.has_correct_fields(field_values.keys(),
                                       mandatory_fields.keys()):
            raise serializers.ValidationError(
                'Incorrect field names, the fields for this Risk Type are: '
                f'{mandatory_fields}'
            )

        for field_name, field_type in mandatory_fields.items():
            type_is_enum = type(field_type) == SupportedTypes.ENUM
            field_value = field_values.get(field_name)
            # Remember: In our representation of Enum type, the type is an
            # actual list with the valid options
            if type_is_enum and field_value not in field_type:
                raise serializers.ValidationError(
                    f'"{field_value}" is not a valid option for {field_name}, '
                    f'valid options are: {field_type}'
                )

            if not type_is_enum\
               and type(field_value) != SupportedTypes.get_type(field_type):
                raise serializers.ValidationError(
                    f'"{field_value}" is not a valid "{field_type}"'
                )

        return data
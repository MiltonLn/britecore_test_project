from decimal import Decimal


class SupportedTypes:
    ENUM = list
    STRING = str
    NUMBER = Decimal
    # We could validate this as a datetime, but we don't want to deal with
    # formats right now, so, let's keep it simple
    DATE = str

    @classmethod
    def atomic_types(cls):
        return ['STRING', 'NUMBER', 'DATE']

    @classmethod
    def check_valid_type(cls, value, field_type):
        type_to_cast = getattr(cls, field_type, None)
        try:
            type_to_cast(value)
            return True
        except Exception:
            return False
class SupportedTypes:
    ENUM = list
    STRING = str
    # This would be better as a decimal, but for simplicity let's keep it as int
    NUMBER = int
    # We could validate this as a datetime, but we don't want to deal with
    # formats right now, so, let's keep it simple
    DATE = str

    @classmethod
    def atomic_types(cls):
        return ['STRING', 'NUMBER', 'DATE']

    @classmethod
    def get_type(cls, type):
        return getattr(cls, type, None)
from flask import abort

def validate_required_fields(data, required_fields):
    missing_fields = [field for field in required_fields if field not in data]
    if missing_fields:
        abort(400, f"Missing required fields: {', '.join(missing_fields)}")

def validate_positive_integer(value, field_name):
    try:
        int_value = int(value)
        if int_value <= 0:
            abort(400, f"{field_name} must be a positive integer")
        return int_value
    except ValueError:
        abort(400, f"{field_name} must be a positive integer")

def validate_boolean(value, field_name):
    if isinstance(value, bool):
        return value
    elif value.lower() == 'true':
        return True
    elif value.lower() == 'false':
        return False
    else:
        abort(400, f"{field_name} must be a boolean value (true or false)")

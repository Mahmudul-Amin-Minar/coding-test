from django.core.exceptions import ValidationError
from django.core.validators import URLValidator

def validate_url(value):
    url_validator = URLValidator()

    if "http://" in value or "https://" in value:
        value = value
    else:
        value = "http://"+ value
    print(value)
    
    try:
        url_validator(value)
    except:
        raise ValidationError("Invalid URL")
    return value
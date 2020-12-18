import re

from django.core.exceptions      import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_phone(value):
    phone_regex     = r"^[a-zA-Z0-9]{4,17}$"
    phone           = re.compile(phone_regex)

    if not phone.match(value):
        raise ValidationError("phone number only input number")

def validate_city(value):
    city_regex  =  r"^[a-zA-Z0080-024F\s\/\-\)\(\`\.\“\‘]+$"
    city        =   re.compile(city_regex)

    if not regex.match(value):
        raise ValidationError(
        _('%(value)s is not a valid number'),
        params = {'value' : value},
        )


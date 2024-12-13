from datetime import datetime
import re

from src.forms.schemes import FormFieldType


async def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

async def validate_phone(phone):
    pattern = r'^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$'
    return re.match(pattern, phone) is not None

async def validate_date(date_str):
    formats = ['%d.%m.%Y', '%Y-%m-%d']
    for fmt in formats:
        try:
            datetime.strptime(date_str, fmt)
            return True
        except ValueError:
            continue
    return False

async def get_field_type(field):
    if await validate_date(field):
        return 'date'
    elif await validate_phone(field):
        return 'phone'
    elif await validate_email(field):
        return 'email'
    else:
        return 'text'

async def change_form_values_to_type(form: dict[str, str]) -> dict[str, FormFieldType]:
        validate_form: dict[str, FormFieldType] = {}

        for key, value in form.items():
            field_type: FormFieldType = await get_field_type(value)
            validate_form[key] = field_type

        return validate_form

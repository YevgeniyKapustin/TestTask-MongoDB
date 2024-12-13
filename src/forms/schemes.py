from pydantic import BaseModel, EmailStr, field_validator
from enum import Enum
from datetime import datetime
import re

class FormFieldType(str, Enum):
    text = "text"
    date = "date"
    phone = "phone"
    email = "email"


# class FormFieldValidator(BaseModel):
#     field_type: str
#     value: str

#     @field_validator('value')
#     def validate_value(cls, v, values):
#         field_type = values.get('field_type')
        
#         if field_type == FormFieldType.email:
#             return EmailStr.validate(v)
        
#         elif field_type == FormFieldType.phone:
#             if not re.match(r'^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$', v):
#                 raise ValueError('Invalid phone format. Please use +7 xxx xxx xx xx.')
#             return v
        
#         elif field_type == FormFieldType.date:
#             try:
#                 datetime.strptime(v, '%d.%m.%Y')
#             except ValueError:
#                 try:
#                     datetime.strptime(v, '%Y-%m-%d')
#                 except ValueError:
#                     raise ValueError('Invalid date format. Use DD.MM.YYYY or YYYY-MM-DD.')
#             return v
        
#         elif field_type == FormFieldType.text:
#             return v
        
#         raise ValueError('Unknown field type.')

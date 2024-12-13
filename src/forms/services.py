from src.database import db
from src.forms.schemes import FormFieldType


async def get_form_by_form(form: dict[str, FormFieldType]) -> dict[str, FormFieldType]:
    matching_form: dict = await db.forms.find_one(form)
    matching_form.pop('_id') if matching_form else ...
    return matching_form

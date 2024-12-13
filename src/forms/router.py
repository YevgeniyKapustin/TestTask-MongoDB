from fastapi import APIRouter, Body
from starlette.status import HTTP_200_OK

from src.forms.schemes import FormFieldType
from src.forms.services import get_form_by_form
from src.forms.utils import change_form_values_to_type

router = APIRouter(
    prefix='',
    tags=['Forms'],
)

@router.post(
    '/get_form',
    name='Get form',
    description='''
    Calculates the name of the most suitable form from the 
    existing ones based on the received form; if no form matches, 
    it returns the validated form.
    ''',
    status_code=HTTP_200_OK,
)
async def get_form(form: dict[str, str]) -> str | dict[str, FormFieldType]:
    typing_form: dict[str, FormFieldType] = await change_form_values_to_type(form)
    result: dict[str, str] | None = await get_form_by_form(typing_form)
    
    if result is None:
        return typing_form

    return result.get('name') if 'name' in result else 'Name is not a noun'

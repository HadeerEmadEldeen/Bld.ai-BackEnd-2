from unittest.loader import VALID_MODULE_NAME
from django.core.exceptions import ValidationError
from django import forms

class  nameValidation(forms.Form):
    name = forms.CharField(max_length=3)

def Validatordescription(value):
    if len(value) <= 10:
        return value
    else:
        raise ValidationError("Description Length Must Be More Than 10 Chars")

class  descriptionValidation(forms.Form):
    description = forms.CharField(validators=[Validatordescription])


    



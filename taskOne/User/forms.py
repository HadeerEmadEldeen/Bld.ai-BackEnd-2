from unittest.loader import VALID_MODULE_NAME
from django.core.exceptions import ValidationError
from django import forms

class  BookForm(forms.Form):
    first_name = forms.CharField(max_length=15)
    last_name = forms.CharField(max_length=15)
    birth_date = forms.DateField()
    email = forms.EmailField()
    password = forms.CharField(max_length=15)
     
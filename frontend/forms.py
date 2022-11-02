from django.forms import ModelForm
from django import forms
from core.models import CandidateTable

from crispy_forms.helper import FormHelper
from crispy_forms.layout import (
    Layout,
    Field,
    Submit,
)



class CandidateTableForm(ModelForm):
    class Meta:
        model = CandidateTable
        fields = '__all__'
        exclude=("skill_keywords_full","candidateFileNamePDF","candidateFileContents")
       

   


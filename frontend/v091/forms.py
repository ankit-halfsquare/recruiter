from django.forms import ModelForm
from django import forms
from core.models import CandidateTable,CandidateResumeTemplates

from easy_select2 import select2_modelform_meta,select2_modelform,apply_select2

from crispy_forms.helper import FormHelper
from crispy_forms.layout import (
    Layout,
    Field,
    Submit,
)


# CandidateTableForm = select2_modelform(CandidateTable)

# CandidateTableForm = select2_modelform(CandidateTable, attrs={'width': '250px'})

# class CandidateTableForm(ModelForm):
#     Meta = select2_modelform_meta(CandidateTable,exclude=("skill_keywords_full","candidateFileNamePDF"))
    

class CandidateTableForm(ModelForm):
    class Meta:
        model = CandidateTable
        fields = '__all__'
        exclude=("skill_keywords_full","candidateFileNamePDF")
        widgets = {
            'field': apply_select2(forms.Select),
        }


class TemplateForm(ModelForm):
    class Meta:
        model = CandidateResumeTemplates
        fields = '__all__'
        



       

   


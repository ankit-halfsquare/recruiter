from django.forms import ModelForm
from core.models import CandidateTable


class CandidateTableForm(ModelForm):
    class Meta:
        model = CandidateTable
        fields = '__all__'
        exclude=("skill_keywords_full","candidateFileNamePDF","candidateFileContents")
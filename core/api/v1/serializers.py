from rest_framework import serializers

from core.models import CandidateTable



class CandidateTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = CandidateTable
        # fields = '__all__'
        exclude = ('active_assignment',)
        # fields = ('id','name', 'company_id')
from rest_framework import serializers

from core.models import CandidateTable,Assignment,Company,Project,Position,Keyword



class CandidateTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = CandidateTable
        # fields = '__all__'
        exclude = ('active_assignment',)
        # fields = ('id','name', 'company_id')


class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = '__all__'
        # exclude = ('active_assignment',)
        # fields = ('id','name', 'company_id')

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = '__all__'




class KeywordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Keyword
        fields = '__all__'
        
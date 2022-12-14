from rest_framework import serializers
from core.models import (
    CandidateTable,Assignment,Company,Project,Position,Keyword,
    CandidateStatus,CandidateSkillLevel,CandidatePriority,PlatformOrReferral
) 


class SkillLevelSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    class Meta:
        model = CandidateSkillLevel
        fields = '__all__'


class CandidateTableSerializer(serializers.ModelSerializer):
    # skillLevel = SkillLevelSerializer(many=True)

    class Meta:
        model = CandidateTable
        depth = 1
        exclude = ("skillLevel",)


class CandidateTableSerializer2(serializers.ModelSerializer):
    class Meta:
        model = CandidateTable
        depth = 0
        exclude = ()

class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = '__all__'

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



class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = CandidateStatus
        fields = '__all__'





class PrioritySerializer(serializers.ModelSerializer):
    class Meta:
        model = CandidatePriority
        fields = '__all__'



class PlatformOrReferralSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlatformOrReferral
        fields = '__all__'


        
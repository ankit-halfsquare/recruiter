from rest_framework import serializers
from core.models import (
    CandidateTable,Assignment,Company,Project,Position,Keyword,
    CandidateStatus,CandidateSkillLevel,CandidatePriority,PlatformOrReferral
) 


class SkillLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CandidateSkillLevel
        fields = ('name',)


class CandidateTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = CandidateTable
        depth = 1
        exclude = ("skillLevel",)


class CandidateTableSerializer2(serializers.ModelSerializer):
    class Meta:
        model = CandidateTable
        depth = 0
        exclude = ()

class CandidateTableSerializer3(serializers.ModelSerializer):
    skillLevel = SkillLevelSerializer(many=True, read_only=True)
    status = serializers.ReadOnlyField(source='status.name')
    priority = serializers.ReadOnlyField(source='priority.name')
    plateformOrReferral = serializers.ReadOnlyField(source='plateformOrReferral.name')
    class Meta:
        model = CandidateTable
        depth = 1
        fields = ('candidate_id','status','priority','plateformOrReferral','year','ww','first_name','last_name','plateformOrReferral','positionOrPerson','refferedBy','skillLevel','specialitySkillSet','semi','intel','project1','project2','project3','activity','pay','skill_keywords_full','phone','email','city','state',)


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


        
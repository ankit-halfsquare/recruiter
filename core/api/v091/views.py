from django.views.decorators.csrf import csrf_exempt

from rest_framework import status,generics
from rest_framework.views import APIView 
from rest_framework.response import Response
from rest_framework.decorators import api_view

from functools import reduce
from operator import or_,and_
from django.db.models import Q

from core.utils import html_start,html_end,convert_html_to_pdf

from core.models import ( 
    CandidateTable,Assignment,Company,Project,Position,Keyword,CandidateStatus,CandidateSkillLevel,
    CandidatePriority,PlatformOrReferral
)
from .serializers import ( 
    CandidateTableSerializer,AssignmentSerializer,CompanySerializer,ProjectSerializer,PositionSerializer,
    KeywordSerializer,StatusSerializer,SkillLevelSerializer,PrioritySerializer,PlatformOrReferralSerializer
)



class CandidateUpdateAPIView(generics.UpdateAPIView):
    queryset = CandidateTable.objects.all()
    serializer_class = CandidateTableSerializer
    lookup_feild = 'pk'

    # def perform_update(self, serializer): # optional if need any modification before
    #     title = serializer.validated_data.get('title')
    #     content = serializer.validated_data.get('content') or None
    #     if content is None: 
    #             content = title
    #     instance = serializer.save(content=content)




class KeywordListCreateAPIView(generics.ListCreateAPIView):
    queryset = Keyword.objects.all()
    serializer_class = KeywordSerializer



class AssignmentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer


class CompanyListCreateAPIView(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class ProjectListCreateAPIView(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer



class PositionListCreateAPIView(generics.ListCreateAPIView):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer


class CandidateRetrieveAPIView(generics.RetrieveAPIView):
    queryset = CandidateTable.objects.all()
    serializer_class = CandidateTableSerializer
    lookup_feild = 'candidate_id'



class CandidateListCreateAPIView(generics.ListCreateAPIView):
    queryset = CandidateTable.objects.all()
    serializer_class = CandidateTableSerializer


class CandidateView(APIView):
    def get(self, request,pk=None, *args, **kwarg):

        def strtolst(obj):
            if obj and "," in obj:
                return obj.split(",")
            return [obj] if obj else []

        queryprms = request.GET

        skills = queryprms.get('skills',"")
        city = queryprms.get('city',"")
        exclude = queryprms.get('exclude',"") 

        if queryprms.get('search'):
            searchname = queryprms.get('search')
        
            query = f"?skills={skills}&city={city}&exclude={exclude}"
            
     
        if skills or city or exclude:
            skills = strtolst(skills) 
            city = strtolst(city) 
            exclude = strtolst(exclude) 
            
            q_object1 = reduce(or_, (Q(skill_keywords_full__icontains=key) for key in skills)) if skills else Q(skill_keywords_full__icontains = "")
            q_object2 = reduce(or_, (Q(city__icontains=key) for key in city)) if city else Q(city__icontains = "")
            q_object3 = reduce(or_, (~Q(skill_keywords_full__icontains=key) for key in exclude)) if exclude else ~Q(skill_keywords_full__icontains = "dummyValue")
            
            q = (Q(q_object1) &Q(q_object2) & Q(q_object3))
            Candidates = CandidateTable.objects.filter(q)
        else:
            Candidates = CandidateTable.objects.all()

        serializer = CandidateTableSerializer(Candidates, many =True)

        return Response({ "data":serializer.data})
       



##v-0.9.1 views


class StatusListCreateAPIView(generics.ListCreateAPIView):
    queryset = CandidateStatus.objects.all()
    serializer_class = StatusSerializer



class SkillLevelListCreateAPIView(generics.ListCreateAPIView):
    queryset = CandidateSkillLevel.objects.all()
    serializer_class = SkillLevelSerializer


class PriorityListCreateAPIView(generics.ListCreateAPIView):
    queryset = CandidatePriority.objects.all()
    serializer_class = PrioritySerializer


class PlatformOrReferralListCreateAPIView(generics.ListCreateAPIView):
    queryset = PlatformOrReferral.objects.all()
    serializer_class = PlatformOrReferralSerializer




class CreateCustomeResume(APIView):
    def post(self, request,pk=None, *args, **kwarg):
        id = request.POST['id']
        html = request.POST['test']
        filename = request.POST['filename']
        convert_html_to_pdf(html, filename)
        return Response({ "data":"data"})

        


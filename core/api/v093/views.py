from django.views.decorators.csrf import csrf_exempt

from rest_framework import status,generics
from rest_framework.views import APIView 
from rest_framework.response import Response
from rest_framework.decorators import api_view

from functools import reduce
from operator import or_,and_
from django.db.models import Q

from core.utils import convert_html_to_pdf,uploadFile,deleteFile

from core.models import ( 
    CandidateTable,Assignment,Company,Project,Position,Keyword,CandidateStatus,CandidateSkillLevel,
    CandidatePriority,PlatformOrReferral
)
from .serializers import ( 
    CandidateTableSerializer,AssignmentSerializer,CompanySerializer,ProjectSerializer,PositionSerializer,
    KeywordSerializer,StatusSerializer,SkillLevelSerializer,PrioritySerializer,PlatformOrReferralSerializer,CandidateTableSerializer2
    
)



class CandidateUpdateAPIView(generics.UpdateAPIView):
    queryset = CandidateTable.objects.all()
    serializer_class = CandidateTableSerializer2
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
    queryset = CandidateTable.objects.filter(Q(archive = False))
    serializer_class = CandidateTableSerializer

    def get_queryset(self):
        archive = self.request.query_params.get('archive')
        print("archive=>1",archive)
        if archive == "True":
            print("archive=>2",archive)
            queryset = CandidateTable.objects.filter(Q(archive = archive))
            return queryset
        else:
            print("archive=3",archive)
            return super().get_queryset()
        


class CandidateView(APIView):
    def get(self, request,pk=None, *args, **kwarg):
        print("CandidateView=====>")
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
        html = request.POST['html']
        filename = request.POST['filename']
        CandidateTable.objects.filter(pk=id).update(template=html)
        convert_html_to_pdf(html, filename)
        deleteFile(filename)
        uploadFile(filename)
        return Response({ "data":"data"})

        


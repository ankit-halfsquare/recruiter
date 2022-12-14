from django.views.decorators.csrf import csrf_exempt

from rest_framework import status,generics
from rest_framework.views import APIView 
from rest_framework.response import Response
from rest_framework.decorators import api_view


from functools import reduce
from operator import or_,and_
from django.db.models import Q
from django.forms.models import model_to_dict

from core.utils import convert_html_to_pdf,uploadFile,deleteFile

from core.models import ( 
    CandidateTable,Assignment,Company,Project,Position,Keyword,CandidateStatus,CandidateSkillLevel,
    CandidatePriority,PlatformOrReferral
)
from .serializers import ( 
    CandidateTableSerializer,AssignmentSerializer,CompanySerializer,ProjectSerializer,PositionSerializer,
    KeywordSerializer,StatusSerializer,SkillLevelSerializer,PrioritySerializer,
    PlatformOrReferralSerializer,CandidateTableSerializer2,CandidateTableSerializer3
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
    # print("CandidateRetrieveAPIView")
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
        


from django.core.serializers.python import Serializer

class MySerialiser(Serializer):
    def end_object( self, obj ):
        self._current['id'] = obj._get_pk_val()
        self.objects.append( self._current )


class CandidateView(APIView):
    def get(self, request,pk=None, *args, **kwarg):
        
        archive = self.request.query_params.get('archive')
        if archive == "True":
            print("archive=>1",archive)
            Candidates = CandidateTable.objects.filter(Q(archive = archive))
        else:
            print("archive=>2",archive)
            Candidates = CandidateTable.objects.filter(Q(archive = False))


        serializer = CandidateTableSerializer3(Candidates, many =True)
      
        data = serializer.data

    
        for d in data:
            skills = d['skillLevel']
            string = ''
            for skill in skills:
                for key in skill:
                    string += skill[key]
                    string += ','

            d['skillLevel'] = string

        return Response({ "data":data})


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




##v-0.9.3 views
class ProjectRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    lookup_feild = 'pk'

    def destroy(self, request, *args, **kwargs):
        # print("ProjectRetrieveUpdateDestroyView")
        return super().destroy(self, request, *args, **kwargs)



class StatusRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CandidateStatus.objects.all()
    serializer_class = StatusSerializer
    lookup_feild = 'pk'

    def destroy(self, request, *args, **kwargs):
        # print("ProjectRetrieveUpdateDestroyView")
        return super().destroy(self, request, *args, **kwargs)



class PlatformOrReferralRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PlatformOrReferral.objects.all()
    serializer_class = PlatformOrReferralSerializer
    lookup_feild = 'pk'

    def destroy(self, request, *args, **kwargs):
        # print("ProjectRetrieveUpdateDestroyView")
        return super().destroy(self, request, *args, **kwargs)


class SkillLevelRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CandidateSkillLevel.objects.all()
    serializer_class = SkillLevelSerializer
    lookup_feild = 'pk'

    def destroy(self, request, *args, **kwargs):
        # print("ProjectRetrieveUpdateDestroyView")
        return super().destroy(self, request, *args, **kwargs)



class PrioritycaRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CandidatePriority.objects.all()
    serializer_class = PrioritySerializer
    lookup_feild = 'pk'

    def destroy(self, request, *args, **kwargs):
        # print("ProjectRetrieveUpdateDestroyView")
        return super().destroy(self, request, *args, **kwargs)



    
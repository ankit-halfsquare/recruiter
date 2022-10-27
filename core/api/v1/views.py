from django.views.decorators.csrf import csrf_exempt

from rest_framework import status,generics
from rest_framework.views import APIView 
from rest_framework.response import Response
from rest_framework.decorators import api_view

from functools import reduce
from operator import or_,and_
from django.db.models import Q

from core.models import CandidateTable
from .serializers import CandidateTableSerializer



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
       




        if obj and "," in obj:
            return obj.split(",")
        return [obj] if obj else []

    

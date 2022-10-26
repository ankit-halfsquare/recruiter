from django.views.decorators.csrf import csrf_exempt

from rest_framework import status,generics
from rest_framework.views import APIView 
from rest_framework.response import Response
from rest_framework.decorators import api_view

from core.models import CandidateTable
from .serializers import CandidateTableSerializer



class CandidateRetrieveAPIView(generics.RetrieveAPIView):
    queryset = CandidateTable.objects.all()
    serializer_class = CandidateTableSerializer
    lookup_feild = 'candidate_id'



class CandidateListCreateAPIView(generics.ListCreateAPIView):
    queryset = CandidateTable.objects.all()
    serializer_class = CandidateTableSerializer
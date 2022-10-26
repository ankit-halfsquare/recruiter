from django.urls import path   
from . import views

urlpatterns = [
    path("candidate/", views.CandidateListCreateAPIView.as_view(), name = "candidate-listCreateAPI-View"),
    path("candidate/<int:pk>/", views.CandidateRetrieveAPIView.as_view(), name = "candidate-retrieveAPI-view"),
]
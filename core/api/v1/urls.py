from django.urls import path   
from . import views

urlpatterns = [
    path("candidate/", views.CandidateView.as_view(), name = "candidate-View"),
    path("candidate-list/", views.CandidateListCreateAPIView.as_view(), name = "candidate-listCreateAPI-View"),
    path("candidate/<int:pk>/", views.CandidateRetrieveAPIView.as_view(), name = "candidate-retrieveAPI-view"),
]
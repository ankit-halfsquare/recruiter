from django.urls import path   
from . import views

urlpatterns = [
    path("candidate/", views.CandidateView.as_view(), name = "candidate-View"),
    path("candidate-list/", views.CandidateListCreateAPIView.as_view(), name = "candidate-listCreateAPI-View"),
    path("candidate/<int:pk>/", views.CandidateRetrieveAPIView.as_view(), name = "candidate-retrieveAPI-view"),
    path("candidate-update/<int:pk>/", views.CandidateUpdateAPIView.as_view(), name = "candidate-updateAPI-view"),

    path("assignment-list/", views.AssignmentListCreateAPIView.as_view(), name = "assignment-listCreateAPI-View"),
    path("company-list/", views.CompanyListCreateAPIView.as_view(), name = "company-listCreateAPI-View"),
    path("project-list/", views.ProjectListCreateAPIView.as_view(), name = "project-listCreateAPI-View"),
    path("position-list/", views.PositionListCreateAPIView.as_view(),name = "position-listCreateAPI-View"),
    path("keyword-list/", views.KeywordListCreateAPIView.as_view(),name = "keyword-listCreateAPI-View"),

]
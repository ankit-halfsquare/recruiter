from django.urls import path   
from . import views

urlpatterns = [
    path("v-0.9.0/candidate/", views.CandidateView.as_view(), name = "v-0.9.0/candidate-View"),
    path("v-0.9.0/candidate-list/", views.CandidateListCreateAPIView.as_view(), name = "v-0.9.0/candidate-listCreateAPI-View"),
    path("v-0.9.0/candidate/<int:pk>/", views.CandidateRetrieveAPIView.as_view(), name = "v-0.9.0/candidate-retrieveAPI-view"),
    path("v-0.9.0/candidate-update/<int:pk>/", views.CandidateUpdateAPIView.as_view(), name = "v-0.9.0/candidate-updateAPI-view"),

    path("v-0.9.0/assignment-list/", views.AssignmentListCreateAPIView.as_view(), name = "v-0.9.0/assignment-listCreateAPI-View"),
    path("v-0.9.0/company-list/", views.CompanyListCreateAPIView.as_view(), name = "v-0.9.0/company-listCreateAPI-View"),
    path("v-0.9.0/project-list/", views.ProjectListCreateAPIView.as_view(), name = "v-0.9.0/project-listCreateAPI-View"),
    path("v-0.9.0/position-list/", views.PositionListCreateAPIView.as_view(),name = "v-0.9.0/position-listCreateAPI-View"),
    path("v-0.9.0/keyword-list/", views.KeywordListCreateAPIView.as_view(),name = "v-0.9.0/keyword-listCreateAPI-View"),

]
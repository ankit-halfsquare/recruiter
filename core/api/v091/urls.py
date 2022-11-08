from django.urls import path   
from . import views

urlpatterns = [
    path("v-0.9.1/candidate/", views.CandidateView.as_view(), name = "v-0.9.1/candidate-View"),
    path("v-0.9.1/candidate-list/", views.CandidateListCreateAPIView.as_view(), name = "v-0.9.1/candidate-listCreateAPI-View"),
    path("v-0.9.1/candidate/<int:pk>/", views.CandidateRetrieveAPIView.as_view(), name = "v-0.9.1/candidate-retrieveAPI-view"),
    path("v-0.9.1/candidate-update/<int:pk>/", views.CandidateUpdateAPIView.as_view(), name = "v-0.9.1/candidate-updateAPI-view"),

    path("v-0.9.1/assignment-list/", views.AssignmentListCreateAPIView.as_view(), name = "v-0.9.1/assignment-listCreateAPI-View"),
    path("v-0.9.1/company-list/", views.CompanyListCreateAPIView.as_view(), name = "v-0.9.1/company-listCreateAPI-View"),
    path("v-0.9.1/project-list/", views.ProjectListCreateAPIView.as_view(), name = "v-0.9.1/project-listCreateAPI-View"),
    path("v-0.9.1/position-list/", views.PositionListCreateAPIView.as_view(),name = "v-0.9.1/position-listCreateAPI-View"),
    path("v-0.9.1/keyword-list/", views.KeywordListCreateAPIView.as_view(),name = "v-0.9.1/keyword-listCreateAPI-View"),


    ##v-0.9.1
    path("v-0.9.1/status-list/", views.StatusListCreateAPIView.as_view(), name = "v-0.9.1/status-listCreateAPI-View"),
    path("v-0.9.1/skill-level-list/", views.StatusListCreateAPIView.as_view(), name = "v-0.9.1/skill-level-listCreateAPI-View"),
    path("v-0.9.1/priority-list/", views.PriorityListCreateAPIView.as_view(), name = "v-0.9.1/priority-listCreateAPI-View"),

]
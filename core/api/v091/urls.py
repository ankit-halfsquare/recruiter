from django.urls import path   
from . import views

urlpatterns = [
    path("candidate/", views.CandidateView.as_view(), name = "v-0.9.1/candidate-View"),
    path("candidate-list/", views.CandidateListCreateAPIView.as_view(), name = "v-0.9.1/candidate-listCreateAPI-View"),
    path("candidate/<int:pk>/", views.CandidateRetrieveAPIView.as_view(), name = "v-0.9.1/candidate-retrieveAPI-view"),
    path("candidate-update/<int:pk>/", views.CandidateUpdateAPIView.as_view(), name = "v-0.9.1/candidate-updateAPI-view"),

    path("assignment-list/", views.AssignmentListCreateAPIView.as_view(), name = "v-0.9.1/assignment-listCreateAPI-View"),
    path("company-list/", views.CompanyListCreateAPIView.as_view(), name = "v-0.9.1/company-listCreateAPI-View"),
    path("project-list/", views.ProjectListCreateAPIView.as_view(), name = "v-0.9.1/project-listCreateAPI-View"),
    path("position-list/", views.PositionListCreateAPIView.as_view(),name = "v-0.9.1/position-listCreateAPI-View"),
    path("keyword-list/", views.KeywordListCreateAPIView.as_view(),name = "v-0.9.1/keyword-listCreateAPI-View"),


    ##v-0.9.1
    path("status-list/", views.StatusListCreateAPIView.as_view(), name = "v-0.9.1/status-listCreateAPI-View"),
    path("skill-level-list/", views.StatusListCreateAPIView.as_view(), name = "v-0.9.1/skill-level-listCreateAPI-View"),
    path("priority-list/", views.PriorityListCreateAPIView.as_view(), name = "v-0.9.1/priority-listCreateAPI-View"),
    path("platform-referral-list/", views.PlatformOrReferralListCreateAPIView.as_view(), name = "v-0.9.1/platform-R-referral-ListCreateAPI-View"),
    path("create-custome-resume/", views.CreateCustomeResume.as_view(), name = "v-0.9.1/create-custome-resume-api-view"),

]
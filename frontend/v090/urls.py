from django.urls import path,include
from . import views


urlpatterns = [
    path('v-0.9.0/', views.dashboard, name='v-0.9.0/dashboard'),
    path('v-0.9.0/candidate', views.candidate, name='v-0.9.0/candidate'),
    path('v-0.9.0/candidate/<int:pk>', views.viewCandidate, name='v-0.9.0/view-candidate'),

    # path('candidate/<int:pk>', views.candidate, name='candidate'),
    path('v-0.9.0/add-candidate', views.addCandidate, name='v-0.9.0/add-candidate'),
    path('v-0.9.0/assignment', views.assignment, name='v-0.9.0/assignment'),
    path('v-0.9.0/company', views.company, name='v-0.9.0/company'),
    path('v-0.9.0/project', views.project, name='v-0.9.0/project'),
    path('v-0.9.0/position', views.position, name='v-0.9.0/position'),
    path('v-0.9.0/keyword', views.keyword, name='v-0.9.0/keyword'),
    path('v-0.9.0/test', views.test, name='v-0.9.0/test'),
    path('v-0.9.0/accounts/login/', views.CustomeLoginView.as_view(), name='v-0.9.0/login'),


    path('v-0.9.0/search', views.searchCandidate, name='v-0.9.0/search-candidate'),
    # path('candidate/add', views.addUpdateCandidate, name='add-candidate'),
    path('v-0.9.0/candidate/update/<int:pk>', views.addUpdateCandidate, name='v-0.9.0/update-candidate'),


    path('v-0.9.0/logout', views.logout, name='v-0.9.0/request-logout'),

    
]
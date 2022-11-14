from django.urls import path,include
from . import views


urlpatterns = [
    
    path('v-0.9.1/candidate', views.candidate, name='v-0.9.1/candidate'),
    path('v-0.9.1/candidate/<int:pk>', views.viewCandidate, name='v-0.9.1/view-candidate'),  
    path('v-0.9.1/add-candidate', views.addCandidate, name='v-0.9.1/add-candidate'),
    path('v-0.9.1/assignment', views.assignment, name='v-0.9.1/assignment'),
    path('v-0.9.1/company', views.company, name='v-0.9.1/company'),
    path('v-0.9.1/project', views.project, name='v-0.9.1/project'),
    path('v-0.9.1/position', views.position, name='v-0.9.1/position'),
    path('v-0.9.1/keyword', views.keyword, name='v-0.9.1/keyword'),
    path('v-0.9.1/test', views.test, name='v-0.9.1/test'),
    path('v-0.9.1/accounts/login/', views.CustomeLoginView.as_view(), name='v-0.9.1/login'),
    path('accounts/login/', views.CustomeLoginView.as_view(), name='login'),
    path('v-0.9.1/search', views.searchCandidate, name='v-0.9.1/search-candidate'),
    path('v-0.9.1/candidate/update/<int:pk>', views.addUpdateCandidate, name='v-0.9.1/update-candidate'),
    path('v-0.9.1/logout', views.logout, name='v-0.9.1/request-logout'),
    path('logout', views.logout, name='request-logout'),

 
    ## New Urls v-0.9.1
    # path('', views.candidates, name='candidates'),
    path('v-0.9.1/', views.candidates, name='v-0.9.1/candidates'),
    path('v-0.9.1/template/', views.template, name='v-0.9.1/template'),
    path('v-0.9.1/status', views.status, name='v-0.9.1/status'),
    path('v-0.9.1/skill-level', views.skillLevel, name='v-0.9.1/skill-level'),
    path('v-0.9.1/priority', views.priority, name='v-0.9.1/priority'),
    path('v-0.9.1/platform-referral', views.platformOrReferral, name='v-0.9.1/platform-referral'),

    
]
from django.urls import path,include
from . import views


urlpatterns = [
    
    path('v-0.9.3/candidate', views.candidate, name='v-0.9.3/candidate'),
    path('v-0.9.3/candidate/<int:pk>', views.viewCandidate, name='v-0.9.3/edit-candidate'),  
    path('v-0.9.3/candidate/<int:pk>', views.viewCandidate, name='v-0.9.3/view-candidate'),  
    path('v-0.9.3/add-candidate', views.addCandidate, name='v-0.9.3/add-candidate'),
    path('v-0.9.3/project', views.project, name='v-0.9.3/project'),
    path('v-0.9.3/test', views.test, name='v-0.9.3/test'),
    path('v-0.9.3/accounts/login/', views.CustomeLoginView.as_view(), name='v-0.9.3/login'),
    path('accounts/login/', views.CustomeLoginView.as_view(), name='login'),
    path('v-0.9.3/search', views.searchCandidate, name='v-0.9.3/search-candidate'),
    path('v-0.9.3/candidate/update/<int:pk>', views.addUpdateCandidate, name='v-0.9.3/update-candidate'),
    path('v-0.9.3/logout', views.logout, name='v-0.9.3/request-logout'),
    path('logout', views.logout, name='request-logout'),

 
    ## New Urls v-0.9.3
    path('', views.candidates, name='candidates'),
    path('v-0.9.3/', views.candidates, name='v-0.9.3/candidates'),
    path('v-0.9.3/template/', views.template, name='v-0.9.3/template'),
    path('v-0.9.3/status', views.status, name='v-0.9.3/status'),
    path('v-0.9.3/skill-level', views.skillLevel, name='v-0.9.3/skill-level'),
    path('v-0.9.3/priority', views.priority, name='v-0.9.3/priority'),
    path('v-0.9.3/platform-referral', views.platformOrReferral, name='v-0.9.3/platform-referral'),

    
]
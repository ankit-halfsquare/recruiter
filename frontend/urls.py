from django.urls import path,include
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('assignment', views.assignment, name='assignment'),
    path('company', views.company, name='company'),
    path('project', views.project, name='project'),
    path('position', views.position, name='position'),
    path('keyword', views.keyword, name='keyword'),


    path('candidate/<int:pk>', views.viewCandidate, name='view-candidate'),
    path('candidate/update/<int:pk>', views.addUpdateCandidate, name='update-candidate'),
    
]
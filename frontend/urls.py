from django.urls import path,include
from . import views


urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('candidate', views.candidate, name='candidate'),
    path('candidate/<int:pk>', views.viewCandidate, name='view-candidate'),

    # path('candidate/<int:pk>', views.candidate, name='candidate'),
    path('add-candidate', views.addCandidate, name='add-candidate'),
    path('assignment', views.assignment, name='assignment'),
    path('company', views.company, name='company'),
    path('project', views.project, name='project'),
    path('position', views.position, name='position'),
    path('keyword', views.keyword, name='keyword'),
    path('test', views.test, name='test'),
    path('accounts/login/', views.CustomeLoginView.as_view(), name='login'),


    path('search', views.searchCandidate, name='search-candidate'),
    # path('candidate/add', views.addUpdateCandidate, name='add-candidate'),
    path('candidate/update/<int:pk>', views.addUpdateCandidate, name='update-candidate'),


    path('logout', views.logout, name='request-logout'),

    
]
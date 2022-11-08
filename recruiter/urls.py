"""recruiter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

admin.site.site_header = "AMWorks Recruiter Administration"
admin.site.site_title = "AMWorks Admin Portal"
admin.site.index_title = "Welcome to AMWorks Researcher Portal"

urlpatterns = [
    path("", include("frontend.v090.urls")),
    path('admin/', admin.site.urls, name='admin'),
    path("accounts/", include("django.contrib.auth.urls")),
    path('core/api/v-0.9.0/', include('core.api.v090.urls')),
]



from django.contrib import admin
from django.urls import path,include
from django.urls import path, reverse_lazy
from django.views.generic.base import RedirectView

admin.site.site_header = "AMWorks Recruiter Administration"
admin.site.site_title = "AMWorks Admin Portal"
admin.site.index_title = "Welcome to AMWorks Recruiter Portal"

urlpatterns = [
    path("", include("frontend.v090.urls")),
    path("", include("frontend.v091.urls")),
    path("", include("frontend.v093.urls")),
    path("admin-panel/", RedirectView.as_view(url=reverse_lazy('admin:index')) , name="admin-panel" ),
    path('admin/', admin.site.urls),
    path('tinymce/', include('tinymce.urls')),
    path("accounts/", include("django.contrib.auth.urls")),
    path('core/api/v-0.9.0/', include('core.api.v090.urls')),
    path('core/api/v-0.9.1/', include('core.api.v091.urls')),
    path('core/api/v-0.9.3/', include('core.api.v093.urls')),
]

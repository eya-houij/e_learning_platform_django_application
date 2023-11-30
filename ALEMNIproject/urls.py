
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path("ALEMNIap/", include('ALEMNIap.urls')),
    path("Student_Portal/", include('Student_Portal.urls')),
    path("Tutor_Portal/", include('Tutor_Portal.urls')),
    path("Authentication_Module/", include('Authentication_Module.urls')),
    path("Course_Management_Module/", include('Course_Management_Module.urls')),
    path("API_Module/", include('API_Module.urls')),
]

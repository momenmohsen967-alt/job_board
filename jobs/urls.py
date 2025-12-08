from django.urls import path
from .views import job_list, job_details

app_name = 'jobs'

urlpatterns = [
    path('', job_list, name="job_list"),
    path('<int:id>', job_details, name="job_details"),
]

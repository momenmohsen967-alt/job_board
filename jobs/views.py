from django.shortcuts import render

# Create your views here.
from .models import Job

def job_list (request):
    jobs = Job.objects.all()
    return render(request, 'jobs.html', {"jobs":jobs})
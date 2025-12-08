from django.shortcuts import render
from .models import Job

def job_list (request):
    jobs = Job.objects.all().only('id',  'image', 'title', 'location', 'job_type', 'created_at')
    return render(request, 'jobs.html', {"jobs":jobs})


def job_details(request, **kwargs):
    job = Job.objects.get(id=kwargs['id'])
    return render(request, 'job_details.html', {"job":job})
from django.db import models
from django.contrib.auth.models import User
JOB_TYPE = (
    ('part_time','part_time'),
    ('full_time','full_time'),
)
LOCATION_TYPE=(
    ('cairo','cairo'),
    ('portsaid','portsaid'),
    ('ElDqhlia','ElDqhlia'),
    ('Damietta','Damietta'),
    ('mansoura','mansoura'),
    ('Kafr EL-Sheikh','Kafr EL-Sheikh')
)


class Job(models.Model):
    user=models.ForeignKey(User, related_name="created_by", null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=30, null=False, blank=False)
    job_type = models.CharField(max_length=10, null=False, blank=False, choices=JOB_TYPE, default=JOB_TYPE[0][0])
    location = models.CharField(max_length=100, null=False, blank=False, choices=LOCATION_TYPE, default=LOCATION_TYPE[0][0])
    description = models.TextField(max_length=500, null=False, blank=False)
    responsibility = models.TextField(max_length=200, null=True, blank=True, default="none")
    qualifications = models.TextField(max_length=200, null=True, blank=True, default="none")
    vacancy = models.IntegerField()
    salary = models.CharField(max_length=10, null=False, blank=False)
    benefits = models.TextField(max_length=200, null=True, blank=True, default="none")
    image = models.ImageField(null=True, blank=True, upload_to='jobs/')
    updated_at = models.DateField(auto_now=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"created_by : {self.user.id} {self.title} {self.description[:15]}...."
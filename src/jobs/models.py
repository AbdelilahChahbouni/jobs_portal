from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
class Job(models.Model):
    title = models.CharField(max_length=200)
    location = models.CharField(max_length=500)
    salary = models.IntegerField()
    job_nature = models.CharField(max_length=500)
    posted_date = models.DateTimeField(default=timezone.now())
    description = models.CharField(max_length=1000)
    user = models.ForeignKey(User, related_name="user_jobs", on_delete=models.SET_NULL ,null=True)




class JobDetail(models.Model):
    pass



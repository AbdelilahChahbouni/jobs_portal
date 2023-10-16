from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
class Job(models.Model):
    title = models.CharField(max_length=200)
    location = models.CharField(max_length=500)
    salary = models.IntegerField(default=0, blank=True)
    job_nature = models.CharField(max_length=500)
    posted_date = models.DateTimeField(default=timezone.now())
    last_date = models.DateTimeField(null=True , blank=True)
    description = models.TextField()
    user = models.ForeignKey(User, related_name="user_jobs", on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100,default="")
    company_description = models.CharField(max_length=500 , default="")
    company_website = models.CharField(max_length=200, default="")


    def __str__(self):
        return self.title



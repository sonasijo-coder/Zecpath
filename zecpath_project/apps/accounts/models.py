from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# 1 .Employer model

class Employer(models.Model):
  user = models.OneToOneField(User,on_delete = models.CASCADE)
  company_name = models.CharField(max_length=255)

  def __str__(self):
    return self.company_name

# 2 . Candidate Model

class Candidate(models.Model):
  user = models.OneToOneField(User,on_delete=models.CASCADE)
  resume = models.FileField(upload_to='resumes/',null=True,blank=True)

  def __str__(self):
    return self.user.username
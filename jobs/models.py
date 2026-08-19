from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# 1 . Job Model

class Job(models.Model):
  title = models.CharField(max_length=100)
  description = models.TextField()
  location = models.CharField(max_length=100)
  posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.title

# 2. Application Model

class Application(models.Model):
  status_choices = [
    ('applied', 'Applied'),
    ('shortlisted', 'Shortlisted'),
    ('rejected', 'Rejected'),
    ('hired', 'Hired'),
  ]
  job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='applications')
  applicant = models.ForeignKey(User, on_delete=models.CASCADE, related_name='applications')
  email = models.EmailField()
  status = models.CharField(max_length=20, choices=status_choices, default='applied')
  applied_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return f"{self.applicant.username} - {self.job.title}"

from django.db import models
from django.utils import timezone

class Developer(models.Model):
  developer_id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=255)
  biography = models.TextField()
  profile_picture_url = models.URLField(blank=True)
  email = models.EmailField(unique=True)
  phone_number = models.CharField(max_length=20, blank=True)
  website_url = models.URLField(blank=True)

  def __str__(self):
    return self.name

class Resource(models.Model):
  resource_id = models.AutoField(primary_key=True)
  title = models.CharField(max_length=255)
  description = models.TextField()
  file_url = models.URLField()
  developer = models.ForeignKey(Developer, on_delete=models.CASCADE)  # Developer who created the resource

  def __str__(self):
    return self.title

class ContactRequest(models.Model):
  contact_request_id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=255)
  email = models.EmailField()
  message = models.TextField()
  created_at = models.DateTimeField(default=timezone.now)

  def __str__(self):
    return f"{self.name} - {self.created_at}"







# Create your models here.



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
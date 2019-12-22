from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class authorpost(models.Model):
    name=models.CharField(max_length=20)
    post_title=models.CharField(max_length=200)
    post_content=models.TextField(default="Tutorial Content")
    date_published=models.DateField(blank=True,null=True)
    user_profile_link=models.TextField(max_length=200)
    
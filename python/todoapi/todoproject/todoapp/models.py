from django.db import models

# Create your models here.
class Todo(models.Model):
    name=models.CharField(max_length=150)
    desc=models.CharField(max_length=150)
    date_created=models.DateTimeField(auto_now=True)
    
from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class List(models.Model):
  list_name = models.CharField(max_length=50, unique=True, blank=False, null=False)
  list_password = models.CharField(max_length=50, blank=False, null=False)
  
  def __str__(self):
    return self.list_name
  
class Task(models.Model):
  list = models.ForeignKey(List, on_delete = models.CASCADE)
  task_name = models.CharField(max_length=200, blank=False, null=False)
  important = models.BooleanField(default=False)
  done = models.BooleanField(default=False)
  
  def __str__(self):
    return self.task_name
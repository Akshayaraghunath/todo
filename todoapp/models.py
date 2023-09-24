from django.db import models
from django.contrib.auth.models import User

class TodoModel(models.Model):
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    file=models.ImageField(upload_to='todo_images',null=True)
    date=models.DateField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)


# Create your models here.

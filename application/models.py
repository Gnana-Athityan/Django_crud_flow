from django.db import models

# Create your models here.
class Task(models.Model):
    Name=models.CharField(null=True,max_length=200)
    Age=models.IntegerField(null=True)
    Time=models.TimeField(null=True)
    Desc=models.TextField(null=True)

    def __str__(self):
        return self.Name

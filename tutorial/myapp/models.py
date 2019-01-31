from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=50)
    email_id=models.CharField(max_length=50)
    city=models.CharField(max_length=21)
    marks=models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return  self.name + "," + self.email_id
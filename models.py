from django.db import models

# Create your models here.
class MyFileUpload(models.Model):
    subject_Name=models.CharField(max_length=50)
    my_file=models.FileField()
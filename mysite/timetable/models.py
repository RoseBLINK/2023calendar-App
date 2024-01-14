from django.db import models

# Create your models here.

class User(models.Model):
    user_id = models.CharField(max_length=20) # test1234
    user_name = models.CharField(max_length=5)
    user_email = models.CharField(max_length=100)

class Subject(models.Model):
    subject_name = models.CharField(max_length=20)
    subject_day = models.CharField(max_length=3)
    subject_start_time = models.TimeField('start data')

class Schedule(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    subject_name = models.ForeignKey(Subject, on_delete=models.CASCADE)


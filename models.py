from django.db import models

class Subject(models.Model):
    subject_name = models.CharField(max_length=100, default='null')
    
    def __str__(self):
        return self.subject_name

class Student(models.Model):
    student_name = models.CharField(max_length=100, default='null')
    grade = models.FloatField()
    remarks = models.CharField(max_length=10, blank=True)
    subject = models.IntegerField()  # Ensure this matches your model

    def __str__(self):
        return self.student_name

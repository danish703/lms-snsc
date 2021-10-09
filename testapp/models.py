from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    class Meta:
        db_table = "course"

    def __str__(self):
        return self.name

class Subject(models.Model):
    subjectName = models.CharField(max_length=100)
    course = models.ForeignKey(Course,related_name="subject_course",on_delete=models.CASCADE)

    class Meta:
        db_table = 'subject'

    def __str__(self):
        return self.subjectName


class Student(models.Model):
    name = models.CharField(max_length=100)
    course = models.ForeignKey(Course,related_name="course",on_delete=models.CASCADE)
    joinDate  = models.DateField()

    class Meta:
        db_table= "students"


    def __str__(self):
        return self.name
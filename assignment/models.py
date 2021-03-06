from django.db import models
from classroom.models import ClassRoom
from myUser.models import User
# Create your models here.
class Assignement(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True,blank=True)
    deadline = models.DateField()
    marks = models.IntegerField(default=100)
    classroom = models.ForeignKey(ClassRoom,on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Submit(models.Model):
    obtainmarks = models.IntegerField()
    submitedAt = models.DateField(auto_now=True)
    assignement = models.ForeignKey(Assignement,on_delete=models.CASCADE)
    student = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.student.fullName
    class Meta:
        unique_together = ('assignement','student')


class Post(models.Model):
    description = models.TextField()
    file = models.FileField(upload_to='files/',blank=True,null=True)
    classroom = models.ForeignKey(ClassRoom,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.description


class Comment(models.Model):
    comment = models.TextField()
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.comment
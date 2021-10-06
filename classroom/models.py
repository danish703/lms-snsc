from django.db import models
from myUser.models import User
# Create your models here.
class ClassRoom(models.Model):
    code = models.CharField(max_length=8,unique=True)
    subject = models.CharField(max_length=100)
    description = models.TextField(null=True,blank=True)
    image = models.ImageField(upload_to='classroom/',blank=True,null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)


    def __str__(self):
        return self.subject



class Enroll(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    classroom = models.ForeignKey(ClassRoom,on_delete=models.CASCADE)
    status = models.BooleanField(default=False)

    class Meta:
        unique_together = ('user','classroom')

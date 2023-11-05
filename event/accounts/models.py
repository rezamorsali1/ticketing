from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ProfileModel(models.Model):
    class Meta:
        verbose_name="user"
        


    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    # name =models.CharField(max_length=20)
    # LastName = models.CharField(max_length=25)
    man =1
    woman =2
    startus_choice =((man,"Male"),(woman,"Female"))
    gender = models.IntegerField(choices= startus_choice)
    profileImage = models.ImageField(upload_to='profileImages/', null=True)
    credit= models.IntegerField(default=0)


    def __str__(self) :
        return f"{self.user.username} 's Profile "

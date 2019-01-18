from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete = models.PROTECT)

    #additional classes

    first_name = models.CharField(blank=True, max_length=100)
    last_name = models.CharField(blank=True, max_length=100)
    email = models.EmailField()
    text = models.CharField(max_length=10000)



    def __str__(self):
        return self.user.username

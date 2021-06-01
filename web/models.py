# Create your models here.
from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #   Other Property
    #age = models.IntegerField(max_length=3)
    #salary = models.IntegerField(max_length=8)

    def __str__(self):
        return self.user.username

from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    pass

    def __str__(self):
        return self.username


class Client(models.Model):
    name = models.CharField(max_length=255, null=True)
    surname = models.CharField(max_length=255, null=True)
    country = models.CharField(max_length=255, null=True)
    #login_of = models.CharField(max_length=255, null=True)
    #password_of = models.CharField(max_length=255, null=True)
    #of_email = models.CharField(max_length=255, null=True)
    #of_password_email = models.CharField(max_length=255, null=True)
    #paid_account = models.BooleanField(default=False)
    #login_of_paid_account = models.CharField(max_length=255, null=True, blank= True)
    #password_of_paid_account = models.CharField(max_length=255, null=True, blank = True)
    #email_of_paid_account = models.CharField(max_length=255, null=True,blank=True)
    #password_of_email_paid_account = models.CharField(max_length=255, null=True, blank=True)
    photo = models.CharField(max_length=255, null=True)
    #telegram_photos_link = models.CharField(max_length=255, null=True)
    managers = models.ManyToManyField(User)


    def __str__(self):
        return f'{self.name} {self.surname}'




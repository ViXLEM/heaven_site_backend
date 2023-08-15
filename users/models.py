from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    project = models.ManyToManyField('core.Project')

    def __str__(self):
        return self.username


def socials_list():
    return {
        'Instagram': [],
        'Facebook': [],
        'Reddit': [],
    }

def project_list():
    return {
        'AnastasiaDating': {
            'eMAIL': 'Hui',
            'Login': 'Privet',
        },
        'DateMe': [],
        'CharmDate': [],
        'GoldenBride': [],
        'Fansly': [],
        'OnlyFans': [],
        'Jump4Love': []
    }


class Client(models.Model):

    name = models.CharField(max_length=255, null=True)
    surname = models.CharField(max_length=255, null=True)
    country = models.CharField(max_length=255, null=True)
    photo = models.CharField(max_length=255, null=True)
    date_of_birth = models.DateField(null=True)
    project_info = models.JSONField(default=project_list)
    socials = models.JSONField(default=socials_list)
    managers = models.ManyToManyField(User)

    def __str__(self):
        return f'{self.name} {self.surname}'

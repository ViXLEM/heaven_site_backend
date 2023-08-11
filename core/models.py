from django.db import models

# Create your models here.

TABLE_TYPE = [
    ('OP', 'OnlyFans'),
    ('FP', 'FreeAccOnlyfans'),
    ('PP', 'PayAccOnlyfans'),
    ('AD', 'AnastasiaDating'),
    ('D', 'Dating')
]

PROJECT_NAMES = [
    ('OF', 'OnlyFans'),
    ('AD', 'AnastasiaDating'),
    ('DM', 'DateMe'),
    ('CD', 'CharmDate'),
    ('J4', 'JumpForLove'),
    ('GB', 'GoldenBride'),
    ('RM', 'RomansCompass'),
    ('PM', 'PrimeDate'),
    ('F', 'Fansly')
]


class Table(models.Model):
    create_date = models.DateField(default='01-01-2023', null=False, auto_now=False)
    client = models.ForeignKey('users.Client', on_delete=models.DO_NOTHING)
    operator = models.ForeignKey('users.User', on_delete=models.DO_NOTHING)
    table_type = models.CharField(choices=TABLE_TYPE, null=True, max_length=50)
    account_id = models.CharField(null=True, max_length=50)
    project = models.ForeignKey('Project', on_delete=models.DO_NOTHING)


class TableData(models.Model):
    date = models.DateField()
    data = models.FloatField(null=True)
    is_day_off = models.BooleanField(default=False)
    table = models.ForeignKey('Table', on_delete=models.CASCADE)


class Project(models.Model):
    site_name = models.CharField(choices=PROJECT_NAMES, max_length=50)

    def __str__(self):
        return self.site_name

# Generated by Django 4.0.6 on 2023-07-04 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_client_managers_alter_client_email_of_paid_account_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='paid_account',
            field=models.BooleanField(default=False),
        ),
    ]

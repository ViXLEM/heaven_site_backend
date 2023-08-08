# Generated by Django 4.0.6 on 2023-07-04 09:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0005_alter_client_paid_account'),
    ]

    operations = [
        migrations.CreateModel(
            name='RomansCompassTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default='01-01-2023')),
                ('account_id', models.CharField(max_length=50)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='users.client')),
                ('operator', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TableData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('data', models.FloatField(null=True)),
                ('table', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='romans_compass.romanscompasstable')),
            ],
        ),
    ]
# Generated by Django 4.0 on 2022-01-18 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Faculty', '0021_assignment_assignment'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignment',
            name='section',
            field=models.CharField(default=None, max_length=10),
        ),
        migrations.AddField(
            model_name='assignment',
            name='sem',
            field=models.CharField(default=None, max_length=10),
        ),
    ]

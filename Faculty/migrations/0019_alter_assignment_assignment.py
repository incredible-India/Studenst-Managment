# Generated by Django 4.0 on 2022-01-18 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Faculty', '0018_assignment_assignment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='assignment',
            field=models.FileField(default=None, upload_to='assignments/'),
        ),
    ]

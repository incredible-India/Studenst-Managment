# Generated by Django 4.0 on 2022-01-18 08:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Faculty', '0019_alter_assignment_assignment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assignment',
            name='assignment',
        ),
    ]
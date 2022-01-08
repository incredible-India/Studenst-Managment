# Generated by Django 4.0 on 2022-01-08 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='sem',
            field=models.CharField(choices=[('1', '1st sem'), ('2', '2nd sem'), ('3', '3rd sem'), ('4', '4th sem'), ('5', '5th sem'), ('6', '6th sem'), ('7', '7th sem'), ('8', '8th sem')], default=None, max_length=10),
        ),
    ]
# Generated by Django 4.0 on 2022-01-11 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0009_alter_student_classteacher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='simg',
            field=models.ImageField(upload_to='Student/img'),
        ),
    ]
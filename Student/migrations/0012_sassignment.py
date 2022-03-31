# Generated by Django 4.0 on 2022-02-02 09:58

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Faculty', '0026_alter_assignment_assignment'),
        ('Student', '0011_alter_student_simg'),
    ]

    operations = [
        migrations.CreateModel(
            name='sAssignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assignment', models.FileField(upload_to='assignments/student/pdf/')),
                ('dueDate', models.DateField(default=datetime.datetime(2022, 2, 2, 9, 58, 54, 979841, tzinfo=utc))),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Faculty.assignment')),
            ],
        ),
    ]
# Generated by Django 4.0 on 2022-01-08 11:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Faculty', '0011_alter_teaches_sem'),
        ('Student', '0004_student_simg'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='classTeacher',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Faculty.teacher'),
        ),
    ]
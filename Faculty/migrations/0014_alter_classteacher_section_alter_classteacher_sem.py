# Generated by Django 4.0 on 2022-01-16 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Faculty', '0013_alter_classteacher_teacher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classteacher',
            name='section',
            field=models.CharField(default=None, max_length=10),
        ),
        migrations.AlterField(
            model_name='classteacher',
            name='sem',
            field=models.CharField(default=None, max_length=10),
        ),
    ]

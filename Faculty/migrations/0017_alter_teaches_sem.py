# Generated by Django 4.0 on 2022-01-16 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Faculty', '0016_alter_teaches_section'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teaches',
            name='sem',
            field=models.CharField(default=None, max_length=10),
        ),
    ]

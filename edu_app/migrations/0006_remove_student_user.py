# Generated by Django 4.0.1 on 2022-01-25 12:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('edu_app', '0005_student'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='user',
        ),
    ]
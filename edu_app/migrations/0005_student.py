# Generated by Django 4.0.1 on 2022-01-25 12:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('edu_app', '0004_events'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=13)),
                ('parents_name', models.CharField(max_length=50)),
                ('blood_group', models.CharField(blank=True, choices=[('A +ve', 'A +'), ('B +ve', 'B +'), ('AB +ve', 'AB +'), ('O +ve', 'O +'), ('O -ve', 'O -')], max_length=10, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

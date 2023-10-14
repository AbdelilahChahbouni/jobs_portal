# Generated by Django 4.2.6 on 2023-10-14 12:38

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='JobDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=500)),
                ('salary', models.IntegerField()),
                ('job_nature', models.CharField(max_length=500)),
                ('posted_date', models.DateTimeField(default=datetime.datetime(2023, 10, 14, 12, 38, 57, 285340, tzinfo=datetime.timezone.utc))),
                ('description', models.CharField(max_length=1000)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_jobs', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
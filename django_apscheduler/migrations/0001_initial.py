# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-11-05 16:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DjangoJob',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=190, unique=True)),
                ('next_run_time', models.DateTimeField(db_index=True)),
                ('job_state', models.BinaryField()),
            ],
            options={
                'ordering': ('next_run_time',),
            },
        ),
        migrations.CreateModel(
            name='DjangoJobExecution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[['Added', 'Added'], ['Started execution', 'Started execution'], ['Max instances reached!', 'Max instances reached!'], ['Missed!', 'Missed!'], ['Modified!', 'Modified!'], ['Removed!', 'Removed!'], ['Error!', 'Error!'], ['Executed', 'Executed']], max_length=50)),
                ('run_time', models.DateTimeField(db_index=True)),
                ('duration', models.DecimalField(decimal_places=2, default=None, max_digits=15, null=True)),
                ('started', models.DecimalField(decimal_places=2, default=None, max_digits=15, null=True)),
                ('finished', models.DecimalField(decimal_places=2, default=None, max_digits=15, null=True)),
                ('exception', models.CharField(max_length=1000, null=True)),
                ('traceback', models.TextField(null=True)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='django_apscheduler.DjangoJob')),
            ],
            options={
                'ordering': ('-run_time',),
            },
        ),
    ]

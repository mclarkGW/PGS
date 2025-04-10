# Generated by Django 5.2 on 2025-04-09 18:21

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='PersonalGoldSource',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('location', models.CharField(choices=[('bangalore', 'Bangalore'), ('canada', 'Canada'), ('chennai', 'Chennai'), ('puerto rico', 'Puerto Rico'), ('usa', 'USA')], max_length=20)),
                ('employeetype', models.CharField(choices=[('regular', 'Regular'), ('contractor', 'Contractor')], max_length=20)),
                ('employeeid', models.IntegerField()),
                ('start_date', models.DateField()),
                ('lwd_date', models.DateField()),
                ('resignation_date', models.DateField()),
                ('ext_leavestart_date', models.DateField()),
                ('ext_leaveend_date', models.DateField()),
                ('status', models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive'), ('resigned', 'Resigned'), ('extended leave', 'Extended Leave')], max_length=20)),
                ('peoplemanager', models.EmailField(max_length=254)),
                ('todaysdate', models.DateField(default=datetime.date.today)),
                ('jobtitle', models.CharField(max_length=100)),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PGS_App.roles')),
            ],
        ),
    ]

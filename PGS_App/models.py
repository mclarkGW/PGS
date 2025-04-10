from datetime import date
from django.db import models


location_choices = [
    ('bangalore', 'Bangalore'),
    ('canada', 'Canada'),
    ('chennai', 'Chennai'),
    ('puerto rico', 'Puerto Rico'),
    ('usa', 'USA'),
]
employeetype_choices = [
    ('regular', 'Regular'),
    ('contractor', 'Contractor'),
]
status_choices = [
    ('active', 'Active'),
    ('inactive', 'Inactive'),
    ('resigned', 'Resigned'),
    ('extended leave', 'Extended Leave'),
]
roletype_choices = [
    ('technical', 'Technical'),
    ('business', 'Business'),
    ('tbd', 'TBD'),
]

class Roles (models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    roletype = models.CharField(max_length=100, choices=roletype_choices, default='tbd')
    def __str__(self):
        return self.title

class PersonalGoldSource(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    location = models.CharField(max_length=20, choices=location_choices, blank=True, null=True)
    employeetype = models.CharField(max_length=20, choices=employeetype_choices, blank=True, null=True)
    employeeid = models.IntegerField(unique=True,blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    lwd_date = models.DateField(blank=True, null=True)
    resignation_date = models.DateField(blank=True, null=True)
    ext_leavestart_date = models.DateField(blank=True, null=True)
    ext_leaveend_date = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=status_choices)
    peoplemanager = models.EmailField(blank=True, null=True)
    todaysdate = models.DateField(default=date.today)
    jobtitle = models.CharField(max_length=100, blank=True, null=True)
    role = models.ForeignKey(Roles, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
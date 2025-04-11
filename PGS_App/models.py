from datetime import date
from django.db import models
from dateutil.relativedelta import relativedelta  # To calculate years and months
from django.core.exceptions import ValidationError # To validate RoleSkill unquieness


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
region_choices = [
    ('canada', 'Canada'),
    ('mexico','Mexico'),
    ('us1', 'US1'),
    ('us2', 'US2'),
    ('us4', 'US4'),
    ('us5', 'US5'),
    ('india', 'India'),

]
yes_no_choices = [
    ('yes','YES'),
    ('no','NO'),
]

class JobLevel (models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.title

class Roles (models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, unique=True)
    roletype = models.CharField(max_length=100, choices=roletype_choices, default='tbd')
    def __str__(self):
        return self.title

class Role_Skill (models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, unique=True)
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
    status = models.CharField(max_length=20, choices=status_choices,default='active')
    peoplemanager = models.EmailField(blank=True, null=True)
    jobtitle = models.CharField(max_length=100, blank=True, null=True)
    role = models.ForeignKey(Roles, on_delete=models.CASCADE)
    joblevel = models.ForeignKey(JobLevel, on_delete=models.CASCADE,blank=True, null=True)
    region = models.CharField(max_length=20, choices=region_choices,blank=True, null=True)
    supplier_name = models.CharField(max_length=100, blank=True, null=True)
    orgunit2_desc = models.CharField(max_length=255, blank=True, null=True)
    orgunit3_desc = models.CharField(max_length=255, blank=True, null=True)
    orgunit4_desc = models.CharField(max_length=255, blank=True, null=True)
    orgunit5_desc = models.CharField(max_length=255, blank=True, null=True)
    orgunit6_desc = models.CharField(max_length=255, blank=True, null=True)
    timeofservice = models.CharField(max_length=50, blank=True, null=True)
    projectmoon = models.CharField(max_length=20,choices=yes_no_choices,default='no')
    shorecalc = models.CharField(max_length=50, blank=True, null=True)
    
    # Updated roleskill fields with unique related_name attributes
    roleskill1 = models.ForeignKey(Role_Skill, on_delete=models.CASCADE, blank=True, null=True, related_name='roleskill1')
    roleskill2 = models.ForeignKey(Role_Skill, on_delete=models.CASCADE, blank=True, null=True, related_name='roleskill2')
    roleskill3 = models.ForeignKey(Role_Skill, on_delete=models.CASCADE, blank=True, null=True, related_name='roleskill3')
    roleskill4 = models.ForeignKey(Role_Skill, on_delete=models.CASCADE, blank=True, null=True, related_name='roleskill4')
    roleskill5 = models.ForeignKey(Role_Skill, on_delete=models.CASCADE, blank=True, null=True, related_name='roleskill5')

    def save(self, *args, **kwargs):
        # Calculate time of service only if start_date is provided
        if self.start_date:
            today = date.today()
            delta = relativedelta(today, self.start_date)  # Get difference in years and months
            self.timeofservice = f"{delta.years} YRS - {delta.months} MTHS"
        else:
            self.timeofservice = None
        
        # Calculate ShoreCalc based on region
        if self.region in ["India", "Canada"]:
            self.shorecalc = "Offshore"
        else:
            self.shorecalc = "Onshore"

        super().save(*args, **kwargs)
    
    def clean(self):
        super().clean()  # Call the parent class's clean method
        # Collect all selected roleskills into a list
        roleskills = [
            self.roleskill1,
            self.roleskill2,
            self.roleskill3,
            self.roleskill4,
            self.roleskill5,
        ]

        # Remove None values (blank fields)
        roleskills = [skill for skill in roleskills if skill is not None]

        # Check for duplicates
        if len(roleskills) != len(set(roleskills)):
            raise ValidationError("Each Role Skill must be unique. Please select different values for each field.")

    def __str__(self):
        return self.name
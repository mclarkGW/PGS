from django import forms
from .models import PersonalGoldSource

class PersonalGoldSourceForm(forms.ModelForm):
    class Meta:
        model = PersonalGoldSource
        fields = ['name', 'email', 'employeeid', 'employeetype', 'peoplemanager', 'location',
                  'jobtitle', 'role', 'start_date', 'lwd_date', 'resignation_date',
                  'ext_leavestart_date', 'ext_leaveend_date', 'status']
        labels = {
            'name': 'Preferred Name',
            'email': 'Email',
            'employeeid': 'Employee ID',
            'employeetype': 'Employee Type',
            'peoplemanager': 'People Manager Email',
            'location': 'Location',
            'jobtitle': 'Job Title',
            'role': 'Role',
            'start_date': 'Start Date',
            'lwd_date': 'LWD Date',
            'resignation_date': 'Resignation Date',
            'ext_leavestart_date': 'Extended Leave Start Date',
            'ext_leaveend_date': 'Extended Leave End Date',
            'status': 'Status',
        }
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'lwd_date': forms.DateInput(attrs={'type': 'date'}),
            'resignation_date': forms.DateInput(attrs={'type': 'date'}),
            'ext_leavestart_date': forms.DateInput(attrs={'type': 'date'}),
            'ext_leaveend_date': forms.DateInput(attrs={'type': 'date'}),
        }
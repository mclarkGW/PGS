from django import forms
from .models import PersonalGoldSource

class PersonalGoldSourceForm(forms.ModelForm):
    class Meta:
        model = PersonalGoldSource
        fields = [
            'name', 'email', 'employeeid', 'employeetype', 'peoplemanager', 'location',
            'joblevel', 'region', 'projectmoon', 'jobtitle', 'supplier_name',
            'orgunit2_desc','orgunit3_desc','orgunit4_desc','orgunit5_desc','orgunit6_desc',
            'start_date', 'timeofservice', 'lwd_date', 'resignation_date',
            'ext_leavestart_date', 'ext_leaveend_date', 'status', 'role', 
            'roleskill1', 'roleskill2', 'roleskill3', 'roleskill4', 'roleskill5','shorecalc',
        ]
        labels = {
            'name': 'Preferred Name',
            'email': 'Email',
            'employeeid': 'Employee ID',
            'employeetype': 'Employee Type',
            'peoplemanager': 'People Manager Email',
            'location': 'Location',
            'joblevel': 'Job Level',
            'region': 'Region',
            'projectmoon': 'Project Moon Hire?',
            'jobtitle': 'Job Title',
            'supplier_name':'Supplier Name',
            'orgunit2_desc':'Org Level 2',
            'orgunit3_desc':'Org Level 3',
            'orgunit4_desc':'Org Level 4',
            'orgunit5_desc':'Org Level 5',
            'orgunit6_desc':'Org Level 6',
            'start_date': 'Start Date',
            'timeofservice': 'Time Of Service',
            'resignation_date': 'Resignation Date',
            'lwd_date': 'LWD',
            'ext_leavestart_date': 'Extended Leave Start Date',
            'ext_leaveend_date': 'Extended Leave End Date',
            'status': 'Status',
            'role': 'Role',
            'roleskill1': 'Role Skill 1',
            'roleskill2': 'Role Skill 2',
            'roleskill3': 'Role Skill 3',
            'roleskill4': 'Role Skill 4',
            'roleskill5': 'Role Skill 5',
            'shorecalc': 'Shore Calculation',
        }
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'lwd_date': forms.DateInput(attrs={'type': 'date'}),
            'resignation_date': forms.DateInput(attrs={'type': 'date'}),
            'ext_leavestart_date': forms.DateInput(attrs={'type': 'date'}),
            'ext_leaveend_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super(PersonalGoldSourceForm, self).__init__(*args, **kwargs)
        # Make timeofservice and shorecalc read-only
        self.fields['timeofservice'].widget.attrs['readonly'] = True
        self.fields['shorecalc'].widget.attrs['readonly'] = True

    def clean(self):
        cleaned_data = super().clean()

        # Validation to ensure Role Skills are unique
        roleskills = [
            cleaned_data.get('roleskill1'),
            cleaned_data.get('roleskill2'),
            cleaned_data.get('roleskill3'),
            cleaned_data.get('roleskill4'),
            cleaned_data.get('roleskill5'),
        ]
        
        # Remove None values
        roleskills = [skill for skill in roleskills if skill is not None]
        
        # Check for duplicates
        if len(roleskills) != len(set(roleskills)):
            raise forms.ValidationError("Each Role Skill must be unique. Please select different values for each field.")

        return cleaned_data
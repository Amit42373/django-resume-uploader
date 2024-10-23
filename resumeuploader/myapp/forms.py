from django import forms
from . models import Resume

GENDER_CHOICES = [
 ('Male', 'Male'),
 ('Female', 'Female')
]

JOB_CITY_CHOICE= [
    ('Delhi', 'Delhi'),
    ('Pune', 'Pune'),
    ('Patna', 'Patna'),
    ('Bangluru', 'Bangluru'),
    ('Noida', 'Noida'),
    ('Gurugram', 'Gurugram'),
]

class ResumeForm(forms.ModelForm):

    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect)
    job_city = forms.MultipleChoiceField(label='Preferred Job Locations', choices=JOB_CITY_CHOICE, widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Resume
        fields = ['name', 'dob', 'gender', 'locality', 'city', 'pin', 'state', 'mobile', 'email','job_city', 'profile_image', 'my_file']

        labels = {'name':'Full Name', 'dob':'Date of Birth', 'mobile':'Mobile No.', 'email':'Email ID', 'profile_image':'Profile Image', 'my_file':'Document'}

        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'dob':forms.DateInput(attrs={'class':'form-control', 'id': 'datepicker'}),
            'mobile':forms.NumberInput(attrs={'class':'form-control'}),
            'locality':forms.TextInput(attrs={'class':'form-control'}),
            'city':forms.TextInput(attrs={'class':'form-control'}),
            'pin':forms.NumberInput(attrs={'class':'form-control'}),
            'state':forms.Select(attrs={'class':'form-select'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
        }
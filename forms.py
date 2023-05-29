from django import forms

class MyFileForm(forms.Form):
    SUBJECT_CHOICES = [
        ('tamil', 'Tamil'),
        ('english', 'English'),
        ('maths', 'Maths'),
        ('physics', 'Physics'),
        ('chemistry', 'Chemistry'),
        ('biology', 'Biology'),
        ('history', 'History'),
        ('economics', 'Economics'),
    ]
    subject_name = forms.ChoiceField(choices=SUBJECT_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    file=forms.FileField(widget=forms.FileInput(attrs={'class':'form-control'}))
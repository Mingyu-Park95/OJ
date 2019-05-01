from django import forms
from django.forms import TextInput


#LANG = ('C', 'C++', 'JAVA', 'Python')


CHOICES = (('C', 'C',), ('C++', 'C++',), ('JAVA', 'JAVA'), ('Python', 'Python'))


class CodeSubmissionForm(forms.Form):
    lang = forms.ChoiceField(widget=forms.Select, choices=CHOICES)
    code = forms.CharField(widget=forms.Textarea(attrs={'rows': 20, 'cols': 70}))



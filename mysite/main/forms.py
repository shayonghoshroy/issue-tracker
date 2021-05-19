from django import forms

class CreateNewList(forms.Form):
    name = forms.CharField(label="Name", max_length = 200)
    check = forms.BooleanField(required=False)

class CreateNewProject(forms.Form):
    name = forms.CharField(label="Name", max_length = 200)
    description = forms.CharField(label="Description", max_length = 1000)

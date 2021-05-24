from django import forms
from . models import Comment, File

class CreateNewList(forms.Form):
    name = forms.CharField(label="Name", max_length = 200)
    check = forms.BooleanField(required=False)

class CreateNewProject(forms.Form):
    name = forms.CharField(label="Name", max_length = 200)
    description = forms.CharField(label="Description", max_length = 1000)

# create a comment for an issue
class CommentForm(forms.ModelForm):
    content = forms.CharField(label="", widget=forms.Textarea(
        attrs ={
            'class':'form-control',
            'placeholder':'Add a comment...',
            'rows':3,
            'cols':50
        }))
    class Meta:
        model = Comment
        fields = ['content']

# upload a file
class FileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = {'file', 'file_name'}

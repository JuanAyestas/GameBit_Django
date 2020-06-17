from django import forms
from .models import Picture

class PictureForm(forms.ModelForm):
   class Meta:
       model = Picture
       fields = ["picture_files"]
       labels = {"picture_files": "Pictures for the Review"}
       widgets = {"picture_files": forms.ClearableFileInput(attrs={"multiple": True})}

from django import forms
from .models import Picture

class PictureForm(forms.ModelForm):
   class Meta:
       model = Picture
       fields = ["picture_files"]
       labels = {"picture_files": """Game's pictures <small class="text-muted">You can add multiple pictures</small><span class="asteriskField">*</span>"""}
       widgets = {"picture_files": forms.ClearableFileInput(attrs={"multiple": True})}

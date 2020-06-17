from django import forms
from picture_bit.models import Picture
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["title", "platform", "thumbnail", "summary", "content"]

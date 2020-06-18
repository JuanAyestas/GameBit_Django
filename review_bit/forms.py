from django import forms
from picture_bit.models import Picture
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["title", "platform", "thumbnail", "summary", "content"]
        labels = {
            "title": "Game's title",
            "platform": """Platform/s <small class="text-muted">Nintendo Switch, PS4, Xbox, etc.</small>""",
            "summary": """General info <small class="text-muted">For example, the game's genre, release date, or just some bit of info.</small>""",
            "content": """Write your review <small class="text-muted">Let them know your opinion!</small>"""
        }

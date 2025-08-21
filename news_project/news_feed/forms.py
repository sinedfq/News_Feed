from django import forms 
from .models import News

# Form for edit object of model News from web-interface
class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ["title", "description", "image"]
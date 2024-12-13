from django import forms
from .models import YourModel
# forms.py



class YourModelForm(forms.ModelForm):
    class Meta:
        model = YourModel
        fields = ['file']  # Include other fields as needed


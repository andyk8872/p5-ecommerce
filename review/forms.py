from .models import Review
from django import forms


class ReviewForm(forms.ModelForm):
    review = forms.CharField(widget=forms.Textarea(), required=True)

    class Meta:
        model = Review
        exclude = ['user',]

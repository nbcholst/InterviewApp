from django import forms
from .models import Choice


class PostAudio(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ('response_file',)

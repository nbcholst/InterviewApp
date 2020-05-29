from django import forms
from .models import audio

class PostAudio(forms.ModelForm):
    class Meta:
        model = audio
        fields = ('recording',)
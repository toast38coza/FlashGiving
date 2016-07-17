from django import forms
from .models import Team


class TeamForm(forms.ModelForm):
    widgets = {
        'campaign': forms.HiddenInput(),
    }
    campaign = forms.CharField(widget=forms.HiddenInput())
    class Meta:
        model = Team
        fields = ['name', 'campaign']


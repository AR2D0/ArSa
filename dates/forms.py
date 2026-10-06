"""
Forms for the Date Mission multi-step flow.
"""
from django import forms
from datetime import date


class DateSelectionForm(forms.Form):
    """Step 2: Select a date."""
    selected_date = forms.DateField(
        widget=forms.DateInput(attrs={
            'type': 'date',
            'class': 'form-control form-control-lg',
            'min': date.today().isoformat(),
        }),
        label='Pick a date',
        required=True,
    )

    def clean_selected_date(self):
        selected = self.cleaned_data['selected_date']
        if selected < date.today():
            raise forms.ValidationError("Please choose a future date ❤️")
        return selected


class TimeSelectionForm(forms.Form):
    """Step 3: Select a time."""
    selected_time = forms.TimeField(
        widget=forms.TimeInput(attrs={
            'type': 'time',
            'class': 'form-control form-control-lg',
        }),
        label='Pick a time',
        required=True,
    )


class LocationSelectionForm(forms.Form):
    """Step 4: Location (text only)."""
    location_name = forms.CharField(
        max_length=255,
        required=True,
        label='Where should we go?',
        widget=forms.TextInput(attrs={
            'class': 'form-control form-control-lg',
            'placeholder': 'e.g. Cafe, Park, Restaurant name...',
        }),
    )

from django import forms

class PropertyForm(forms.Form):
    name = forms.CharField(label='Property Name', max_length=100)
    payment_details = forms.CharField(label='How to Pay', max_length=150)

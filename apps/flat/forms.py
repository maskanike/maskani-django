from django import forms

class FlatForm(forms.Form):
    name = forms.CharField(label='Flat Name', max_length=100)

from django import forms

class url(forms.Form):
    url = forms.URLField(required=True,label='', 
                    widget=forms.TextInput(attrs={'placeholder': 'Link Youtube....'}))

 

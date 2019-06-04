from django import forms


class NameForm(forms.Form):
    nombre = forms.CharField(label='nombre', max_length=100)
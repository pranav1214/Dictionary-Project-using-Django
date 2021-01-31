from django import forms

class DictForm(forms.Form):
	word = forms.CharField(label="Enter Word")
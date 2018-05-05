from django import forms


class SubmitEmployee(forms.Form):
    name = forms.CharField(max_length=100)
    # title = forms.CharField(max_length=50)
    # bio = forms.Textarea()
    # avatar = forms.ImageField()

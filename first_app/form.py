from django import forms
from first_app.models import FormUser


class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)

    def save(self):
        FormUser.objects.get_or_create(name=self.cleaned_data['name'], email=self.cleaned_data['email'], text=self.cleaned_data['text'])

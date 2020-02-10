from django import forms 


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=150, required=True)
    email = forms.CharField(max_length=180, required=True)
    comment = forms.CharField(widget=forms.Textarea, required=True)

from django import forms
from .models import NewsLetterUserList, SendEmailToNewsLetterUser
from tinymce import TinyMCE


class TinyMCEWidget(TinyMCE):
    def use_required_attribute(self, *args):
        return False


class NewsLetterUserListForm(forms.ModelForm):
    email = forms.CharField(label='search',
                            widget=forms.TextInput(attrs={'placeholder': 'Email'}))

    class Meta:
        model = NewsLetterUserList
        fields = ['email']


class SendEmailToNewsLetterUserForm(forms.ModelForm):
    body = forms.CharField(widget=TinyMCEWidget(
        attrs={'required': False, 'cols': 10, 'rows': 10})
    )

    class Meta:
        model = SendEmailToNewsLetterUser
        fields = ['subject', 'body', 'status']

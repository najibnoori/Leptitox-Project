

from django.shortcuts import render
from django.views.generic.base import TemplateView
from newsletter.forms import NewsLetterUserListForm
from contact.forms import ContactForm


class HomePageView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['subscribe_form'] = NewsLetterUserListForm()
        context['contact_form'] = ContactForm()
        return context


class AboutView(TemplateView):
    template_name = 'about.html'
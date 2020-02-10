from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['email']
            comment = form.cleaned_data['comment']
            try:
                send_mail(subject, comment, from_email,
                          ['ab.basir.payenda@gmail.com'])
            except BadHeaderError:
                return HttpResponse('There was a bad request')
            return redirect('leptitox:home')
    else:
        form = ContactForm()
    return render(request, 'contact-form.html', {'contact_form': form})


def contact_success(request):
    return render(request, 'contact-success.html')

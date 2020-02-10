from django.shortcuts import render, redirect
from django.conf import settings
from .models import NewsLetterUserList, SendEmailToNewsLetterUser
from .forms import NewsLetterUserListForm, SendEmailToNewsLetterUserForm
from django.contrib import messages
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import get_template
from django.utils.safestring import mark_safe
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def newsletter_subscribe(request):
    if request.method == 'POST':
        form = NewsLetterUserListForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            if NewsLetterUserList.objects.filter(email=instance.email).exists():
                messages.warning(request, 'This email is already registered!')
            else:
                instance.save()
                subject, recipient_list = 'Subscribed Successfully', [
                    instance.email]
                from_email = settings.EMAIL_HOST_USER
                message = EmailMultiAlternatives(
                    subject=subject, body=None, from_email=from_email, to=recipient_list)
                temp = get_template('subscribe-email.html').render()
                message.attach_alternative(temp, 'text/html')
                message.send()
                messages.success(
                    request, 'You successfully subscribed to our newsletter, please check your email')
                return redirect('leptitox:home')
    else:
        form = NewsLetterUserListForm()
    return render(request, 'index.html', {'subscribe_form': form})


def newsletter_unsubscribe(request):
    form = NewsLetterUserListForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        if NewsLetterUserList.objects.filter(email=instance.email).exists():
            NewsLetterUserList.objects.filter(email=instance.email).delete()
            messages.success(request, 'We\'re sad to see you go :(')
            return redirect('blog-home')
        else:
            messages.success(request, 'Email doesn\'t exists!')

    return render(request, 'unsubscribe.html', {'unsubscribe_form': form})


@login_required
def send_newsletter(request):
    form = SendEmailToNewsLetterUserForm(request.POST or None)
    if form.is_valid():
        instance = form.save()

        if instance.status == 'Published':
            subject = instance.subject
            body = instance.body
            from_email = settings.EMAIL_HOST_USER

            for newsletter_obj in NewsLetterUserList.objects.all():
                msg = EmailMultiAlternatives(
                    subject, body, from_email, [newsletter_obj.email])
                msg.attach_alternative(body, "text/html")
                msg.send()

            return redirect('leptitox:home')
            messages.success(request, 'Email sent successfully!')

    return render(request, 'send-newsletter.html', {'form': form})

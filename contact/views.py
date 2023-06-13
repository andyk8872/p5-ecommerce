from django.shortcuts import render, redirect
from django.views import View
from .models import Contact
from .forms import ContactForm
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.contrib import messages


def contact(request):
    """
    Displays the contact form,
    sends the information collected.
    """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            email = form.cleaned_data['email']

            html = render_to_string('contact/emails/contactform.html', {
                'subject': subject,
                'message': message,
                'email': email
            })

            send_mail('The contact form subject ', 'This is the message\
                ', 'noreply@gmail.com\
                    ', ['scotsteven008@gmail.com'], html_message=html)
            messages.success(
                request, 'Contact message posted.'
                )
            return redirect('contact')
    else:
        form = ContactForm()

    context = {
        'form': form
    }
    return render(request, 'contact/contact.html', context)

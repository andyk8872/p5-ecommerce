from django.shortcuts import render
from django.views import View
from .models import Contact
from .forms import ContactForm


def contact(request):
    """
    Displays the contact form.
    """

    form = ContactForm(request.POST)

    context = {
        'form': form
    }
    return render(request, 'contact/contact.html', context)

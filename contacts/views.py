from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages

from .forms import ContactForm, ContactUpdateForm
from .models import Contact
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic.edit import DeleteView


def contact_form(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # form_instance = form.save(commit = False)
            form.save()
            messages.success(request, "We've received your message. We shall get back to you shortly.")
            
            # send_mail(
            #     subject = "Contact Form Message.",
            #     message = "You have just been sent a message via the website Kindly log in to read and update the message status",
            #     from_email = settings.EMAIL_HOST_USER,
            #     recipient_list = ['admin@valueagrosynergy.com']
            # )

            return redirect('contacts:contact_form')
    context = {
        'form': form,
    }
    return render(request, 'contacts/contact_form.html', context)


@login_required
def contact_messages(request):
    contact_messages = Contact.objects.order_by('-created_at')
    context = {
        'contact_messages': contact_messages
    }
    return render(request, 'contacts/contact_messages.html', context)


@login_required
def message_details(request, id):
    message_details = get_object_or_404(Contact, id=id)
    context = {
        'message_details': message_details
    }
    return render(request, 'contacts/message_details.html', context)


@login_required
def message_update(request, id):
    message = get_object_or_404(Contact, id = id)
    form = ContactUpdateForm(instance = message)
    if request.method == 'POST':
        form = ContactUpdateForm(request.POST, instance = message)
        if form.is_valid():
            form.save()
            messages.success(request, "Changes saved.")
            return redirect('contacts:contact_messages')
    context = {
        'form': form,
        'message': message
    }
    return render(request, 'contacts/message_update.html', context)


class MessageDeleteView(LoginRequiredMixin, DeleteView):
    model = Contact
    template_name = 'contacts/message_delete.html'
    success_url = reverse_lazy('contacts:contact_messages')
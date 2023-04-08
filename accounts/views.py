import random
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model, authenticate, login, logout

from django.core.paginator import Paginator
from django.conf import settings
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import DeleteView

# from .token import account_activation_token
# from django.template.loader import render_to_string
# from django.contrib.sites.shortcuts import get_current_site
# from django.utils.encoding import force_bytes, force_text
# from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

from contacts.models import Contact

from .models import Account, Profile

from .forms import (
    StaffUserCreateForm,
    UserAccountEditForm,
    UserProfileEditForm,
    UserRoleEditForm,
)

User = get_user_model()


@login_required
def dashboard(request):
    unread_messages = Contact.objects.filter(status = "pending")
    context = {
        'unread_messages': unread_messages
    }
    return render(request, 'accounts/dashboard.html', context)


@login_required
def profile(request):

    context = {

    }
    return render(request, 'accounts/profile.html', context)


# Staff User Creation Form
@login_required
def staff_user_create(request):
    form = StaffUserCreateForm()
    if request.method == 'POST':
        form = StaffUserCreateForm(request.POST, request.FILES or None)
        if form.is_valid():
            user = form.save(commit = False)
            user.set_password(f'{random.randint(0, 1000000000)}')
            user.save()
                        
            message = """
            You have been added as a staff of Value Agro. 
            Please go to the log in page and click the forget password link to reset your password to enable you log in to start working.
            """
            send_mail(
                subject = "Staff User Registration.",
                message = message,
                from_email = settings.EMAIL_HOST_USER,
                recipient_list = [user.email,]
            )
            messages.success(request, f'User, {user.username} has successfully been created.')
            return redirect('accounts:staff-user-create')
        else:
           messages.error(request, 'Invalid form entries. Check and try again.') 

    context = {
        'form': form,
    }
    return render(request, 'accounts/staff-user-create.html', context)


# This page is viewed by the Admin HR
@login_required
def user_details(request, username):
    user = get_object_or_404(User, username = username)
    context = {
        'user': user
    }
    return render(request, 'accounts/user-details.html', context)


@login_required
def user_role_edit(request, id):
    user = get_object_or_404(User, id = id)
    form = UserRoleEditForm(instance=user)
    if request.method == 'POST':
        form = UserRoleEditForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Saved.')
            return redirect('accounts:users')
        else:
           messages.error(request, 'Check the form and try again.') 

    context = {
        'user': user,
        'form': form,
    }
    return render(request, 'accounts/user-role-edit.html', context)


@login_required
def user_account_edit(request):
    form = UserAccountEditForm(instance=request.user)
    user_profile_form = UserProfileEditForm(instance = request.user.profile)

    if request.method == 'POST':
        form = UserAccountEditForm(request.POST, request.FILES or None, instance=request.user)
        user_profile_form = UserProfileEditForm(request.POST, request.FILES or None, instance=request.user.profile)
        if form.is_valid() and user_profile_form.is_valid():
            form.save()
            user_profile_form.save()
            messages.success(request, 'Changes saved.')
            return redirect('accounts:user-account-edit')
        else:
           messages.error(request, 'Check the form and try again.') 

    context = {
        'form': form,
        'user_profile_form': user_profile_form
    }
    return render(request, 'accounts/user-account-edit.html', context)


class UserDeleteView(LoginRequiredMixin, DeleteView):
    model = User
    template_name = 'accounts/user-delete.html'
    success_url = reverse_lazy('accounts:users')

from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import SetPasswordForm
from django.shortcuts import render, redirect

from vira.Form.UserForm import UserForm

@login_required
def change_user(request):

    user_form=UserForm(request.POST or None,instance=request.user)
    password_form=SetPasswordForm(request.user)

    if request.method == "POST":
        password_form = SetPasswordForm(request.user, request.POST)
        if user_form.is_valid():
            user_form.save(request)
        if password_form.is_valid():
            request.user.set_password(password_form.cleaned_data['new_password1'])
            request.user.save()
            return redirect('accounts:logout')


    return render(request, 'User/user.html',{
        'user_form':user_form,
        'password_form':password_form,
    })
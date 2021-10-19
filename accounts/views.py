from urllib.parse import urlparse

from django.contrib import auth, messages
from django.contrib.auth import logout
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth.models import  User
from django.core.mail import EmailMultiAlternatives
from django.db import transaction
from django.shortcuts import render, redirect

from accounts.models import Forgot

def login(request):
    if request.user.is_authenticated is True:
        return redirect('vira:view_main')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('vira:view_main')
        else:
            return redirect('accounts:logout')
    return render(request, 'login.html')


def pagelogout(request):
    logout(request)
    return redirect('accounts:login')

def updateUrlProfile(request):
    if request.method == 'GET':

        try:

            data = request.GET.get('query')
            forgot = Forgot.objects.get(uuid=data)
            user = forgot.user
            password_form = SetPasswordForm(user)
            if forgot.status == False:
                forgot.status = True
                forgot.save()
                return render(request, 'newPassword.html',
                              {'password_form': password_form})
            return redirect('accounts:login')

        except:
            return redirect('accounts:login')

    if request.method == 'POST':
        with transaction.atomic():
            try:
                forgot = Forgot.objects.get(uuid=request.GET.get('query'))
                password_form = SetPasswordForm(forgot.user, request.POST)
                user = forgot.user
                if password_form.is_valid():
                    user.set_password(password_form.cleaned_data['new_password1'])
                    user.save()
                    # zaman kontrolüde yapilacak
                    forgot.status = True
                    messages.success(request, 'Şifre Başarıyla Güncellenmiştir.')

                    return redirect('accounts:login')


                else:

                    messages.warning(request, 'Alanları Kontrol Ediniz')
                    return render(request, 'newPassword.html',
                                  {'password_form': password_form})
            except:
                return redirect('accounts:login')

    return render(request, 'accounts/index.html')


def forgot(request):
    if request.method == 'POST':
        mail = request.POST.get('username')
        if User.objects.filter(username=mail):
            user=User.objects.get(username=mail)
            fdk = Forgot(user=user, status=False)
            fdk.save()
            url = urlparse(request.META.get('HTTP_REFERER')).hostname

            html_content = ''
            subject, from_email, to = 'Bilgi Sistemi Kullanıcı Bilgileri', 'fatih@kobiltek.com', mail
            html_content = '<h2>ADALET BAKANLIGI PROJE TAKİP  SİSTEMİ</h2>'
            html_content = html_content + '<p><strong>Kullanıcı Adınız :' + str(fdk.user.username) + '</strong></p>'
            if url == 'kobiltek.com':
                html_content = html_content + '<p> <strong>Yeni şifre oluşturma linki:</strong> <a href="http://www.kobiltek.com:81/yks/sbs/newpassword?query=' + str(
                    fdk.uuid) + '">http://www.kobiltek.com:81/yks/sbs/profil-guncelle/?query=' + str(
                    fdk.uuid) + '</p></a>'
            else:
                html_content = html_content + '<p> <strong>Site adresi:</strong> <a href="http://127.0.0.1:8000/newpassword?query=' + str(
                    fdk.uuid) + '">http://127.0.0.1:8000/sbs/profil-guncelle/?query=' + str(fdk.uuid) + '</p></a>'



            msg = EmailMultiAlternatives(subject, '', from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()

            messages.success(request, "Giriş bilgileriniz mail adresinize gönderildi. ")
            return redirect("accounts:login")
        else:
            messages.warning(request, "Geçerli bir mail adresi giriniz.")
            return redirect("accounts:forgot")

    return render(request, 'forgot-password.html')

from .models import *
from .forms import *
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib import messages


def mail(request):
    if request.method == 'POST':
        form = SendMailForm(request.POST)
        if form.is_valid():
            mail = send_mail(form.cleaned_data['subject'], form.cleaned_data['content'], 'fakelazzex@gmail.com', [form.cleaned_data['name']],)
            if mail:
                messages.success(request, 'Message sent!')
                return redirect('main_page')
            else:
                messages.error(request, 'Fail!')
    else:
        form = SendMailForm()
    return render(request, 'sender/main_page.html', {'form':form})
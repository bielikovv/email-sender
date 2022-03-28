from .models import *
from .forms import *
from django.core.mail import send_mail
from django.shortcuts import render, redirect


def mail(request):
    if request.method == 'POST':
        form = SendMailForm(request.POST)
        if form.is_valid():
            send_mail(form.cleaned_data['subject'], form.cleaned_data['content'], 'fakelazzex@gmail.com', ['ivanbelikov890@gmail.com'], )
            return redirect('main_page')
    else:
        form = SendMailForm()
    return render(request, 'sender/main_page.html', {'form':form})
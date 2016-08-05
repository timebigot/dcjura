from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail, BadHeaderError
#from django.contrib.auth.decorators import login_required
#from django.contrib.auth.models import User
#from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from base.models import *
import datetime

def index(request):
    coupons = Coupon.objects.all().order_by('-pk')
    return render(request, 'index.html', {'coupons': coupons, 'today': datetime.date.today()})

def join(request):
    if request.user.is_authenticated():
        return redirect('/')
    else:
        if request.method == 'GET':
            next = request.GET.get('next')
        return render(request, 'join.html', {'next': next})

"""
def log_in(request):
    next = request.GET.get('next')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                if not next:
                    return redirect('/')
                else:
                    return redirect(next)
            else:
                return HttpResponse('activate your account')
        else:
            messages.error(request, 'Wrong username/password')
            return redirect('/join')
    else:
        # not a POST method
        return redirect('/')

def sign_up(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        repassword = request.POST.get('repassword')

        if not password == repassword:
            messages.error(request, 'Passwords do not match')
            return redirect('join')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username is taken')
            return redirect('join')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email in use')
            return redirect('join')

        user = User.objects.create_user(username, email, password)
        user.save()
        messages.success(request, 'Account created! Please LOGIN!')
        return render(request, 'join.html')
    else:
        return redirect('/')

@login_required
def log_out(request):
    logout(request)
    return redirect('/')
"""

def coupon(request, url_code):
    coupon = Coupon.objects.get(url_code=url_code)
    return render(request, 'coupon.html', {'coupon': coupon, 'modal': True})

def map(request):
    if request.method == 'GET':
        url_code = request.GET.get('url_code')
        coupon = Coupon.objects.get(url_code=url_code)
        return render(request, 'map.html', {'coupon': coupon})
    else:
        return HttpResponse('error')
"""
def contact(request):
    if request.method == 'POST':
        subject = request.POST.get('subject', '')
        reason = request.POST.get('reason', '')
        message = request.POST.get('message')
        from_email = request.POST.get('from_email', '')
        if subject and reason and message and from_email:
            subject = reason + ': ' + subject
            message = from_email + ': ' + message
            try:
                send_mail(subject, message, from_email, ['contact.dcjura@gmail.com'])
            except BadHeaderError:
                return redirect('/')
            else:
                messages.success(request, 'Message sent!')
                return render(request, 'contact.html')
        else:
            return HttpResponse('Make sure all fields are entered and valid.')
    else:
        return render(request, 'contact.html')
"""

from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail, BadHeaderError
from django.http import JsonResponse
from django.core import serializers
from django.db.models import Q
#from django.contrib.auth.decorators import login_required
#from django.contrib.auth.models import User
#from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from base.models import *
import datetime
from django.utils import timezone

today = datetime.date.today()

def index(request):
    all_coupons = Coupon.objects.all().order_by('-pk')
    return render(request, 'index.html', {'all_coupons': all_coupons})

def numbers(request):
    if request.user.is_superuser:
        views = View.objects.filter(is_admin=False).order_by('-pk')
        queries = Query.objects.all().order_by('-pk')
        return render(request, 'numbers.html', {'views':views, 'queries':queries})
    else:
        return redirect('/')

"""
def join(request):
    if request.user.is_authenticated():
        return redirect('/')
    else:
        if request.method == 'GET':
            next = request.GET.get('next')
        return render(request, 'join.html', {'next': next})

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
            messages.warning(request, 'Make sure all fields are entered and valid.')
            return render(request, 'contact.html')
    else:
        return render(request, 'contact.html')

def coupon(request, url_code):
    coupon = Coupon.objects.get(url_code=url_code)
    category = coupon.category
    if not request.user.is_superuser:
        view = View(coupon=coupon)
    else:
        view = View(coupon=coupon, is_admin=True)
    view.save()
    return render(request, 'coupon.html', {'coupon': coupon, 'share_page': True})

def category(request, category):
    category = Category.objects.get(slug=category)
    coupons = Coupon.objects.filter(category=category).order_by('-pk')
    all_coupons = Coupon.objects.all().order_by('-pk')
    return render(request, 'index.html', {'coupons': coupons, 'all_coupons': all_coupons, 'category': category, 'today': today})

def modal(request, url_code):
    coupon = Coupon.objects.get(url_code=url_code)
    if not request.user.is_superuser:
        view = View(coupon=coupon)
    else:
        view = View(coupon=coupon, is_admin=True)
    view.save()
    return render(request, 'modal.html', {'coupon':coupon})

def search(request, query=''):
    if request.method == 'POST':
        if not query:
            return redirect('/')
        else:
            query = request.POST.get('query')
            return redirect('/search/' + query)
    else:
        if not query:
            empty_results = True
        else:
            if not request.user.is_superuser:
                query_log = Query(query=query)
            else:
                query_log = Query(query=query, is_admin=True)
            query_log.save()

            c = Coupon.objects
            coupons = c.filter(
                Q(title__icontains=query) |
                Q(category__eng_name__icontains=query) |
                Q(category__kor_name__icontains=query) |
                Q(business__name__icontains=query)
                ).order_by('-pk')
            coupons = coupons.exclude(exp_date__lte=today)
            if not coupons:
                empty_results = True
            else:
                empty_results = False
    all_coupons = Coupon.objects.all().order_by('-pk')
    return render(request, 'index.html', {'coupons': coupons, 'search': query, 'all_coupons': all_coupons, 'empty_results': empty_results})

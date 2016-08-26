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
from bs4 import BeautifulSoup
import urllib.request
from base.helper import *

today = datetime.date.today()

def index(request):
    cat_online = Category.objects.get(eng_name='Online')
    all_coupons = Coupon.objects.all().exclude(category=cat_online).order_by('-pk')
    return render(request, 'index.html', {'all_coupons': all_coupons})

def numbers(request):
    if request.user.is_superuser:
        views = View.objects.filter(is_admin=False).order_by('-pk')
        queries = Query.objects.filter(is_admin=False).order_by('-pk')
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

    if coupon.category.eng_name == 'Online':
        return redirect(coupon.link)
    else:
        return render(request, 'coupon.html', {'coupon': coupon, 'share_page': True})

def category(request, category):
    category = Category.objects.get(slug=category)
    coupons = Coupon.objects.filter(category=category).order_by('-pk')
    cat_online = Category.objects.get(eng_name='Online')
    all_coupons = Coupon.objects.all().exclude(category=cat_online).order_by('-pk')
    return render(request, 'index.html', {'coupons': coupons, 'all_coupons': all_coupons, 'category': category, 'today': today})

def process(request, url_code):
    coupon = Coupon.objects.get(url_code=url_code)
    if not request.user.is_superuser:
        view = View(coupon=coupon)
    else:
        view = View(coupon=coupon, is_admin=True)
    view.save()
    return render(request, 'process.html', {'coupon':coupon})

def search(request, query=''):
    if request.method == 'POST':
        query = request.POST.get('query')
        if not query:
            return redirect('/')
        else:
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

def scraper(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            url = request.POST.get('url')
            title = request.POST.get('title')

            domain = 'http://www.couponpx.com'
            con = urllib.request.urlopen(url).read()
            soup = BeautifulSoup(con, 'html.parser')

            sel = '#bd > div.rd.rd_nav_style2.clear > div.rd_body.clear > div.xe_content.rd_gallery > a'

            anchor = soup.select(sel)[0]
            link = anchor['href']

            img = anchor.find('img')['src']
            cover_link = domain + img

            business = soup.find('td', class_='store').text

            url_code = url_coder(7)

            cover = thumb_maker(cover_link, is_url=True)

            category = Category.objects.get(eng_name='Online')
            try:
                biz = Business.objects.get(name=business)
            except Business.DoesNotExist:
                biz = Business(name=business)
                biz.save()

            try:
                Coupon.objects.get(title=title, link=link)
            except Coupon.DoesNotExist:
                new = Coupon(title=title, link=link, business=biz, category=category, url_code=url_code, cover=cover)
            else:
                messages.error(request, 'This coupon already exists')
                return render(request, 'scraper.html')

            if soup.find('td', class_='expires'):
                expires = soup.find('td', class_='expires').text
                exp_date = datetime.datetime.strptime(expires, '%Y-%m-%d')
                new.exp_date = exp_date

            new.save()
            return redirect('/category/online')
        else:
            return render(request, 'scraper.html')
    else:
        return redirect('/')

def adminpost(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            name = request.POST.get('name')
            address = request.POST.get('address')
            phone = request.POST.get('phone')

            try:
                Business.objects.get(name=name)
            except Business.DoesNotExist:
                logo = request.FILES['logo']
                logo = thumb_maker(logo, is_url=False)
                business = Business(name=name, address=address, phone=phone, logo=logo)
                business.save()
            else:
                business = Business.objects.get(name=name)


            title = request.POST.get('title')
            category = request.POST.get('category')
            category = Category.objects.get(slug=category)
            cover = request.FILES['cover']
            cover = thumb_maker(cover, is_url=False)
            url_code = url_coder(7)

            try:
                Coupon.objects.get(title=title, business=business)
            except Coupon.DoesNotExist:
                exp_date = request.POST.get('exp_date')
                if exp_date:
                    exp_date = datetime.datetime.strptime(exp_date, '%Y-%m-%d')
                    coupon = Coupon(title=title, category=category, exp_date=exp_date, url_code=url_code, cover=cover, business=business)
                else:
                    coupon = Coupon(title=title, category=category, url_code=url_code, cover=cover, business=business)
                coupon.save()
                messages.success(request, 'Posted coupon succesfully')
                return redirect('/')
            else:
                messages.error(request, 'This coupon already exists')
                return redirect('/adminpost')
        else:
            categories = Category.objects.all().order_by('kor_name').exclude(eng_name='Online')
            return render(request, 'adminpost.html', {'categories':categories})
    else:
        return redirect('/')

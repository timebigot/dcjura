from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def index(request):
    return render(request, 'index.html')

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

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.


def signin(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'login.html', {'pass': 'fail'})
    else:
        return render(request, 'login.html', {'pass': 'ok'})


def signup(request):
    if request.method == 'POST':
        user = User.objects.create_user(username=request.POST['email'], password=request.POST['password'],
                                        email=request.POST['email'], first_name=request.POST['fname'], last_name=request.POST['lname'])

        user.save()
        return redirect('/login')

    else:
        return render(request, 'signup.html')


def signout(request):
    logout(request)
    return redirect('/')

from django.shortcuts import render, redirect

# Create your views here.


def homepage(request):
    if request.user.is_authenticated:
        return redirect('/app')
    else:
        return render(request, 'home.html')


def privacy(request):
    return render(request, 'privacy.html')

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
from .models import Record


def home(request):

    record = Record.objects.all()
    if request.method == 'POST':

        username = request.POST['Username']
        password = request.POST['Password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request=request, user=user)
            # print(request.user.username)

            messages.success(request, "You have logged in")
            # request.session['record'] = record

            return redirect('home')
            # return render(request, 'home.html', {'record': record})

        else:
            messages.success(request, "Error logging in. Please try again...")
            return redirect('home')
    else:

        return render(request, 'home.html', {'record': record})


def logout_user(request):
    logout(request)
    messages.success(request, "Logged out successfully")
    return redirect('home')


def register_user(request):

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "Succesfully registered")
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form': form})
    return render(request, 'register.html', {'form': form})


def user_profile(request, pk):
    if request.user.is_authenticated:
        print(pk)
        record = Record.objects.get(rollno=pk)
        return render(request, 'profile.html', {'record': record})
    else:
        messages.success(request, "You must log in to view profile")
        redirect('home.html')

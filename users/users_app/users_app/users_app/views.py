from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            message = "You have Successfully Signed In"
            return render(request, 'registration/home.html', {'message': message})
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})  

def home(request):
    message = "you have logged in Successfully"
    return render(request,'registration/home.html',{'message1':message})

def sort(request):
    user_list = User.objects.order_by('username')
    paginator = Paginator(user_list, 3)
    page = request.GET.get('page')
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        users = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        users = paginator.page(paginator.num_pages)
    return render(request , 'list_users.html', {'users' : users})

def list_users(request):
    user_list = User.objects.all()
    paginator = Paginator(user_list, 3)
    page = request.GET.get('page')
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        users = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        users = paginator.page(paginator.num_pages)
    return render(request , 'list_users.html', {'users' : users})
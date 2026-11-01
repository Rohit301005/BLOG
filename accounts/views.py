from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
# from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
from . forms import RegisterForm, LoginForm
# from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout


def register(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/post/home')
    else:
        if request.method == "POST":
            form = RegisterForm(request.POST)
            if form.is_valid:
                print('Form errors:', form.errors)
                print("Non-field errors:", form.non_field_errors)
                form.save()
                return HttpResponseRedirect(reverse('home'))
        else:
            form = RegisterForm()
        context = {
                'form':form,
            }
        return render(request,'accounts/register.html',context)
    


def auth_login(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/post/home')
    else:
        if request.method == "POST":
                form = LoginForm(request=request,data=request.POST)
                if form.is_valid():
                    username = form.cleaned_data['username']
                    password = form.cleaned_data['password']
                    user = authenticate(username=username, password=password)
                    if user is not None:
                        login(request, user)
                        homeurl = reverse('home')
                        return HttpResponseRedirect(homeurl)
        else:             
            form = LoginForm()
        context = {
                'form':form,
            }
        return render(request,'accounts/login.html',context)


def auth_logout(request):
    logout(request)
    return HttpResponseRedirect('/accounts/login')
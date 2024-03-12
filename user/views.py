from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login as auth_login,logout as auth_logout
from .forms import RegisterForm,LoginForm
from django.http import HttpResponseRedirect

# Create your views here.

def register(request):

    context = {

        'title': 'Register',

        'form': RegisterForm()

    }

    if request.method == 'POST':

        if request.POST['password'] != request.POST['confirm_password']:

            context['error'] = 'Passwords do not match'

            return render(request, 'register.html', context)

        else:

            form = RegisterForm(request.POST, request.FILES)

            if form.is_valid():

                user = form.save()

                user.set_password(user.password)

                user.save()

                return redirect('index')

    return render(request, 'register.html', context)



        


def login(request):
     context = {
         'title':'Login',
         'form':LoginForm()
     }
     if request.method == 'POST':

        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth_login(request,user)
            return redirect('index')
        else:
            context['error'] = 'Invalid username or password'
     return render(request,'login.html',context=context)
    


def logout(request):
    auth_logout(request)
    return redirect('index')
     
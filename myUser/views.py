from django.shortcuts import render,redirect,HttpResponseRedirect
from .form import UserCreationForm,LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def signin(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        user = authenticate(email=email,password=password)
        if user is not None:
            login(request,user)
            if user.isTeacher:
                return redirect('teacherDashboard')
            elif user.isStudent:
                return redirect('studentDashboard')
            logout(request)
            messages.add_message(request,messages.ERROR,"login with either student or teacher")
            return redirect('signin')
        messages.add_message(request,messages.ERROR,"email and password does not match")
    return render(request,'login.html',context={'form':form})

def signuTeacher(request):
    form = UserCreationForm(request.POST or None)
    print(request.POST)
    if form.is_valid():
        user = form.save()
        user.isTeacher = True
        user.isStudent = False
        user.set_password(request.POST['password'])
        user.save()
        messages.add_message(request,messages.SUCCESS,"signup successfully")
        return redirect('signin')
    context = {
        'form':form
    }
    return render(request,'teacher/signup.html',context)

def signupStudent(request):
    form = UserCreationForm(request.POST or None)
    print(request.POST)
    if form.is_valid():
        user = form.save()
        user.isTeacher = False
        user.isStudent = True
        user.set_password(request.POST['password'])
        user.save()
        messages.add_message(request, messages.SUCCESS, "signup successfully")
        return redirect('signin')
    context = {
        'form': form
    }
    return render(request, 'student/signup.html', context)


@login_required(login_url='signin')
def studentDashboard(request):
    if request.user.isStudent:
        return render(request,'student/dashboard.html')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required(login_url='signin')
def teacherDashboard(request):
    if request.user.isTeacher:
        return render(request,'teacher/dashboard.html')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def signout(request):
    logout(request)
    return redirect('signin')
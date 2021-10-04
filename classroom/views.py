from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import CreateClassRoom
from .models import ClassRoom
import random
import string
from django.contrib import messages
def generateRandomAlphaNumericCode(l=6):
    code = ''.join(random.choice(string.ascii_lowercase+string.digits) for i in range(l))
    return code

# Create your views here.
@login_required(login_url='signin')
def createClassroom(request):
    if request.user.isTeacher:
        form = CreateClassRoom(request.POST or None,request.FILES or None)
        if form.is_valid():
            classroom = form.save(commit=False)
            while(True):
                try:
                    classroom.code = generateRandomAlphaNumericCode()
                    classroom.user = request.user
                    classroom.save()
                    messages.add_message(request,messages.SUCCESS,"Classroom created")
                    return redirect('teacherDashboard')
                except:
                    pass
        context = {
            'form':form
        }
        return render(request,'classroom/create.html',context)
    else:
        return redirect('studentDashboard')


@login_required(login_url='signin')
def classSearch(reqeust):
    if reqeust.user.isStudent:
        code = reqeust.GET['code']
        context = {}
        try:
            classroom = ClassRoom.objects.get(code=code)
            context.update({'classroom':classroom})
        except:
            messages.add_message(reqeust,messages.ERROR,"No class found")
        return render(reqeust,'student/searchresult.html',context)
    return redirect('teacherDashboard')

from django.shortcuts import render,redirect,get_object_or_404,HttpResponse
from .forms import AssignmentForm
from django.contrib import messages
from .models import Assignement
from django.contrib.auth.decorators import login_required
from .mail import sendMail
from classroom.models import Enroll
# Create your views here.

@login_required(login_url='signin')
def assignment(request,id):
    if request.user.isTeacher:
        form = AssignmentForm(request.POST or None)
        assignment = Assignement.objects.filter(classroom_id=id)
        if form.is_valid():
            data = form.save(commit=False)
            data.classroom_id=id
            data.save()
            users = Enroll.objects.filter(classroom_id=id)
            for u in users:
                sendMail(email=u.user.email,name=u.user.fullName,message="Assignment is assigned to you")
            messages.add_message(request,messages.SUCCESS,"Assigned")
            return redirect('assignment',id)
        context = {
            'form':form,
            'assignment':assignment
        }
        return render(request,'teacher/assignment.html',context)
    return redirect('signin')

@login_required(login_url='signin')
def assignmentEdit(request,id):
    if request.user.isTeacher:
        assignment = get_object_or_404(Assignement,id=id)
        form = AssignmentForm(request.POST or None,instance=assignment)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,"Updated")
            return redirect('assignment',assignment.classroom.id)
        context = {
            'form':form,
            'assignment':assignment
        }
        return render(request,'teacher/assignmentEdit.html',context)

@login_required(login_url='signin')
def assignmentDel(request,id):
    if request.user.isTeacher:
        assignment = get_object_or_404(Assignement,id=id)
        classroomid = assignment.classroom.id
        assignment.delete()
        messages.add_message(request,messages.SUCCESS,"deleted")
        return redirect('assignment',classroomid)




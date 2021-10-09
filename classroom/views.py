from django.contrib.auth import login
from django.shortcuts import render,redirect,HttpResponseRedirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import CreateClassRoom
from .models import ClassRoom,Enroll
import random
import string
from django.contrib import messages
from assignment.forms import PostCreateForm,CommentForm
from assignment.models import Post,Comment
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
            try:
                e = Enroll.objects.get(classroom=classroom,user=reqeust.user)
                if e.status:
                    context.update({'joined': 'Already joined'})
                else:
                    context.update({'joined':'requested'})
            except:
                context.update({'joined':'not join'})
            context.update({'classroom':classroom})
        except:
            messages.add_message(reqeust,messages.ERROR,"No class found")
        return render(reqeust,'student/searchresult.html',context)
    return redirect('teacherDashboard')


@login_required(login_url='signin')
def joinClass(request,id):
    if request.user.isStudent:
        enroll = Enroll(user=request.user,classroom_id=id)
        try:
            enroll.save()
            messages.add_message(request,messages.SUCCESS,"Successfully enrolled")
        except Exception as e:
            messages.add_message(request,messages.ERROR,"You have alreadly enrolled")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        return redirect('teacherDashboard')



@login_required(login_url='sigin')
def courseDetails(request,id):
    if request.user.isTeacher:
        form = PostCreateForm(request.POST or None,request.FILES or None)
        posts = Post.objects.filter(classroom_id=id)
        commentForm = CommentForm()
        comment = Comment.objects.all()
        if form.is_valid():
            form = form.save(commit=False)
            form.classroom_id = id
            form.user_id = request.user.id
            form.save()
            messages.add_message(request,messages.SUCCESS,"Posted successfully")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        context = {}
        context.update({'posts':posts})
        context.update({'form':form})
        context.update({'commentform':commentForm})
        context.update({'comments':comment})
        try:
            classroom = ClassRoom.objects.get(id=id)
            enrollStudent = Enroll.objects.filter(classroom=classroom)
            context.update({
                'classroom':classroom,
                'students':enrollStudent,
            })
        except Exception as e:
            messages.add_message(request,messages.ERROR,str(e))
        return render(request,'teacher/courseDetails.html',context)
    else:
        return redirect('studentDashboard')

@login_required(login_url='signin')
def accept(request,id):
    if request.user.isTeacher:
        try:
            e = Enroll.objects.get(id=id)
            e.status = True
            e.save()
            messages.add_message(request,messages.SUCCESS,"Accepted")
        except Exception as e:
            messages.add_message(request,messages.ERROR,str(e))
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        return redirect('studentDashboard')


@login_required(login_url='signin')
def blogEdit(request,id):
    blog = get_object_or_404(Post,id=id)
    form = PostCreateForm(request.POST or None,request.FILES or None,instance=blog)
    if form.is_valid():
        form.save()
        messages.add_message(request,messages.SUCCESS,"Updated successfully")
        return redirect('courseDetails',blog.classroom.id)
    context = {
        'form':form
    }
    return render(request,'teacher/blogedit.html',context)

@login_required(login_url='signin')
def deleteBlog(request,id):
    blog = get_object_or_404(Post,id=id)
    blog.delete()
    messages.add_message(request,messages.SUCCESS,"Deleted")
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required(login_url='signin')
def postComment(request,id):
    commentForm = CommentForm(request.POST)
    if commentForm.is_valid():
        form = commentForm.save(commit=False)
        form.post_id = id
        form.user = request.user
        form.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
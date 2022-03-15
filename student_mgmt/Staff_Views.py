from django.shortcuts import render,redirect
from studentapp.models import*

def Instructor_Dashboard(request):
    Instructor=request.user
    if Staff.objects.all()==Instructor:
        while(True):
         return render(request, 'Staff/instructor-dashboard.html' , {'Instructor':Instructor})
    else:
        context={
            'Instructor':Instructor
        }
    return render(request, 'Staff/instructor-dashboard.html' , context)


def Instructor_My_course(request):
    course=Course.objects.all()
    Instructor=CustomUser.objects.all()
    return render(request, 'Staff/instructor-manage-course.html' , {'course':course , 'Instructor':Instructor})

def Instructor_Earning(request):
    Instructor=CustomUser.objects.all()
    return render(request, 'Staff/instructor-earning.html',{'Instructor':  Instructor})

def Instructor_Student(request):
    Instructor=CustomUser.objects.all()
    return render(request, 'Staff/Instructor_Student.html',{'Instructor':  Instructor})

def Instructor_Orders(request):
    Instructor=CustomUser.objects.all()
    return render(request, 'Staff/instructor-order.html',{'Instructor':  Instructor})

def Instructor_Reviews(request):
    Instructor=CustomUser.objects.all()
    return render(request, 'Staff/instructor-review.html',{'Instructor':  Instructor})

def Instructor_Edit_Profile(request):
    Instructor=CustomUser.objects.all()
    return render(request, 'Staff/instructor-edit-profile.html',{'Instructor':  Instructor})

def Instructor_Payout(request):
    Instructor=CustomUser.objects.all()
    return render(request, 'Staff/instructor-payout.html',{'Instructor':  Instructor})

def Instructor_Settings(request):
    Instructor=CustomUser.objects.all()
    return render(request, 'Staff/instructor-setting.html',{'Instructor':  Instructor})

def Instructor_Delete_Profile(request):
    Instructor=CustomUser.objects.all()
    return render(request, 'Staff/instructor-delete-account.html',{'Instructor':  Instructor})

def Instructor_Sign_Out(request):
    Instructor=CustomUser.objects.all()
    return render(request, 'login.html',{'Instructor':  Instructor})

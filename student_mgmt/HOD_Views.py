from audioop import add
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from studentapp.models import Course,Session_Year,CustomUser,Student,Staff
from django.contrib import messages
# from  studentapp.forms import Form_data
from django.contrib.auth.models import User
@login_required(login_url='/')
def HOME(request):
      return render(request, 'Hod/home.html')

#######Courses###########

def all_courses(request):
    if 'search' in request.POST:
        search=request.POST['search']
        course=Course.objects.filter(course_name__icontains=search)
    else:   
     course=Course.objects.all()
    return render(request, 'HOD/admin-course-list.html',{'course':course})

def course_cateegory(request):
    return render(request, 'HOD/admin-course-category.html')



def course_detail(request):
    course = Course.objects.all()
    return render(request, 'HOD/admin-course-detail.html',{'course':course})


def ADD_COURSE(request):
    if request.method == "POST":
            profile_course_pic=request.FILES.get('profile_course_pic')
            print(profile_course_pic,"kasim")
            course_name=request.POST.get('course_name')
            instructor_name=request.POST.get('instructor_name')
            course_price=request.POST.get('course_price')
            course_title=request.POST.get('course_title')
            course_description=request.POST.get('course_description')
        # print(course_name)
            course = Course(course_name=course_name, course_price=course_price ,
             instructor_name=instructor_name ,profile_course_pic=profile_course_pic,course_title=course_title,course_description=course_description)
            if Course.objects.filter(course_name=course_name).exists():
                messages.warning(request, "This Course Already Exists")
                return HttpResponseRedirect("/HOD/Course/Add/")
            course.save()
            messages.success(request,"Course Are Successfully Created")
            return redirect('add_course')
    else:
      return render(request, 'HOD/add-course.html')



def EDIT_COURSE(request,id):
    course = Course.objects.get(id=id)
    context = {
        'course':course,

    }
    return render(request, 'HOD/edit_course.html',context)


def UPDATE_COURSE(request):
    if request.method =="POST":
        profile_course_pic=request.FILES.get('profile_course_pic')
        print(profile_course_pic,"kasim")
        course_name=request.POST.get('course_name')
        instructor_name=request.POST.get('instructor_name')
        course_price=request.POST.get('course_price')
        course_id = request.POST.get('course_id')

        # print(name,course_id)
           
        course = Course.objects.get(id=course_id)
        course.instructor_name=instructor_name
        course.profile_course_pic=profile_course_pic
        course.course_name = course_name
        course.course_price=course_price
        course.save()
        messages.success(request,'Course are successfully updated')
        return redirect('course_detail')
    return render(request, 'HOD/edit_course.html')

def DELETE_COURSE(request,id):
    course = Course.objects.get(id=id)
    course.delete()
    messages.success(request,"Course are successfully Deleted")
    return redirect('course_detail')


# def ADD_COURSE(request):
#     if request.method == "POST":
#         course_name = request.POST.get("course_name")
#         course_price = request.POST.get("course_price")
#         # print(course_name)
#         course = Course(name=course_name, course_price=course_price)
#         course.save()
#         messages.success(request,"Course Are Successfully Created")
#         return redirect('add_course')
#     return render(request, 'HOD/add-course.html')


 ##ADDSTUDENT########

@login_required
def ADD_STUDENT(request):
    course = Course.objects.all()
    
    session_year = Session_Year.objects.all()
    
    context = {
        'course':course,
        'session_year':session_year
    }

    # print(course)
    # print(session_year)

    if request.method == "POST":
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        course_id    = request.POST.get('course_id')
        session_year_id = request.POST.get('session_year_id')
       
        # print(profile_pic,first_name,last_name,email,username,password,address,gender,course_id,session_year_id)

        if CustomUser.objects.filter(email = email).exists():
            messages.warning(request, "Email is already Taken")
            return redirect('add_student')

        if CustomUser.objects.filter(username = username).exists():
            messages.warning(request, "Username is already Taken")
            return redirect('add_student')
        
        else:
            user = CustomUser(
                first_name = first_name,
                last_name = last_name,
                username = username,
                email = email,
                profile_pic = profile_pic,
                user_type = 3
            )
            user.set_password(password)
            user.save()

            course = Course.objects.get(id=course_id)
            session_year = Session_Year.objects.get(id = session_year_id)

            student = Student(
                profile_img = profile_pic,
                admin = user,
                address = address,
                gender = gender,
                course_id = course,
                session_year_id = session_year,

                
 
            )
            student.save()
            messages.success(request, user.first_name + "  "+ user.last_name + ' Are Successfully Added !!' )
            return redirect('add_student')

    return render(request, 'Hod/add_student.html', context)

def VIEW_STUDENT(request):
    student = Student.objects.all()
    
    context = {
        'student':student,
        
    }
    return render(request, 'HOD/view_student.html', context)    

def EDIT_STUDENT(request,id):
    student = Student.objects.filter(id=id)
    course = Course.objects.all()
    session_year = Session_Year.objects.all()

    context = {
        'student': student,
        'course':course,
        'session_year':session_year
    }
    return render(request, 'HOD/edit_student.html', context)


def UPDATE_STUDENT(request):
    if request.method == "POST":
        student_id = request.POST.get('student_id')
        print(student_id)
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        course_id = request.POST.get('course_id')
        session_year_id = request.POST.get('session_year_id')
        user = CustomUser.objects.get(id=student_id)
       
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.username = username

        if password !=None and password != "":
            user.set_password(password)
        if profile_pic != None and profile_pic !="":
            user.profile_pic = profile_pic
        
        user.save()

        student = Student.objects.get(admin=student_id)
        student.address = address
        student.gender = gender

        course = Course.objects.get(id = course_id)
        student.course = course

        session_year = Session_Year.objects.get(id = session_year_id)
        student.session_year_id = session_year
        student.save()
        messages.success(request, "Record Are Successfully Updated")
        return redirect('view_student')

        
    return render(request, 'HOD/edit_student.html')   

def DELETE_STUDENT(request,admin):
    student = CustomUser.objects.get(id=admin)
    student.delete()
    messages.success(request,"Record are Successfully Deleted")
    return redirect('view_student')
    # return None  

 ##ADD-INSTRUCTOR########

def add_instructor(request):
    if request.method == "POST":
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        qualification = request.POST.get('Qualification')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        # print(profile_pic,first_name,last_name,email,username,password,address,gender,course_id,session_year_id)
        if CustomUser.objects.filter(email = email).exists():
            messages.warning(request, "Email is already Taken")
            return redirect('add_instructor')

        if CustomUser.objects.filter(username = username).exists():
            messages.warning(request, "Username is already Taken")
            return redirect('add_instructor')
        
        else:
            user = CustomUser(
                first_name = first_name,
                last_name = last_name,
                username = username,
                email = email,
                profile_pic = profile_pic,
                user_type = 2
            )
            user.set_password(password)
            user.save()
            instructor = Staff(
                profile_image = profile_pic,
                admin = user,
                address = address,
                gender = gender,
                qualification=qualification,
                
                )
            instructor.save()
            messages.success(request, user.first_name + "  "+ user.last_name + ' Are Successfully Added !!' )
            return redirect('add_instructor')

    return render(request, 'Hod/add_instructor.html')


def VIEW_INSTRUCTOR(request):
    if 'search' in request.POST:
        search=request.POST['search']
        ins = Staff.objects.all()
        instructor=Staff.objects.filter(qualification__icontains=search)
    else:     
     instructor = Staff.objects.all()
    return render(request, 'HOD/view_instructor.html',{'instructor':instructor}) 

def VIEWES(request):
    instructor = Staff.objects.all()
    return render(request, 'Staff/include/banner.html',{'instructor':instructor}) 


def EDIT_INSTRUCTOR(request,id):
    instructor = Staff.objects.filter(id=id)
    context = {
        'instructor': instructor,
        
    }
    return render(request, 'HOD/edit_instructor.html', context)



def UPDATE_INSTRUCTOR(request):
    if request.method == "POST":
        instructor_id = request.POST.get('instructor_id')
        print(instructor_id)
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        qualification = request.POST.get('Qualification')
        address = request.POST.get('address')
        gender = request.POST.get('gender')

        user = CustomUser.objects.get(id=instructor_id)
       
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.username = username

        if password !=None and password != "":
            user.set_password(password)
        if profile_pic != None and profile_pic !="":
            user.profile_pic = profile_pic
        
        user.save()

        instructor = Staff.objects.get(admin=instructor_id)
        instructor.address = address
        instructor.gender = gender
        instructor.qualification = qualification
        instructor.save()
        messages.success(request, "Record Are Successfully Updated")
        return redirect('/HOD/instructors')
    return render(request, '/HOD/edit_instructor.html')   

def DELETE_INSTRUCTOR(request,admin):
    instructor = CustomUser.objects.get(id=admin)
    instructor.delete()
    messages.success(request,"Record are Successfully Deleted")
    return redirect('/HOD/instructors')




#########ADMIN/HOD##########        

def admin_students_list(request):
    return render(request, 'HOD/admin-student-list.html')
def instructors(request):
    return render(request, 'HOD/admin-instructor-list.html')
def instructors_detail(request):
    return render(request, 'HOD/admin-instructor-detail.html')
def instructors_requests(request):
    return render(request, 'HOD/admin-instructor-request.html')
def admin_reviews(request):
    return render(request, 'HOD/admin-review.html')
def admin_earnings(request):
    return render(request, 'HOD/admin-earning.html')
def admin_settings(request):
    return render(request, 'HOD/admin-setting.html')


def Student_list(request):
    student=Student.objects.all()
    course=Course.objects.all()
    return render(request, 'HOD/admin-student-list.html',{'student':student , 'course':course})

#HOD POFILE
def hod_profile(request):
    course=Course.objects.all()
    instructor = Staff.objects.all()
    student = Student.objects.all()
    user=CustomUser.objects.all()
    return render(request, 'HOD/hod_profile.html',{'course':course,'instructor': instructor , 'student':student,'user':user})


#HOD UPDATE

def HOD_UPDATE(request,id):
    hod = CustomUser.objects.filter(id=id)
    context = {
        'hod': hod,
    }
    return render(request, 'HOD/hod_update.html', context)


###SIGNUP#######
from studentapp.forms import RegistrationFormUser
def sign_up(request):
    if request.method=='POST':
        form=RegistrationFormUser(request.POST or None)
        if form.is_valid():
            form.save()
    else:
        form= RegistrationFormUser()       
    return render(request , 'HOD/sign-up.html' , {'form':form})      
          
        
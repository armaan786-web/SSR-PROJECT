from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import redirect,render
from studentapp.EmailBackend import EmailBackend
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from studentapp.models import Course,Staff
# from import Customer, Product, Cart, OrderPlaced

from django.contrib.auth.decorators import login_required

def LOGIN(request):
    return render(request, 'login.html')
    
@login_required(login_url='doLogin')
def  Buy_Course(request , id):
    course = Course.objects.filter(pk=id)
    print(course)
    context ={
        'course':course
    }
    
    return render(request, 'Homepage/checkout.html',context)






def Add_To_Cart(request):
    return render(request, 'Homepage/addtocart.html')

def CourseDetail(request,pk):
   user=request.user
   print(user) 
   if request.method=='POST':
     course=Course.objects.get(id=pk)
   else:    
     course=Course.objects.all().filter(id=pk)
     pic = Staff.objects.all().filter(id=pk)
   return render(request, 'Homepage/course-detail.html',{'course':course,'pic':pic , 'user':user})

# def add_to_cart(request,book_id):
        # if request.user.is_authenticated():
#             try:
#               course = course.objects.get(pk=book_id)
#             except ObjectDoesNotExist:
#                 pass
#             else :
#                 try:
#                     cart = Cart.objects.get(user = request.user, active = True)
#                 except ObjectDoesNotExist:
#                     cart = Cart.objects.create(user = request.user)
#                     cart.save()
#                     cart.add_to_cart(book_id)
#                     return redirect('cart')
#                 else:
#                     return redirect('course')


# def remove_from_cart(request, course_id):
#     if request.user.is_authenticated():
#         try:
#             Course = Course.objects.get(id=pk)
#         except ObjectDoesNotExist:
#             pass 
#         else:
#             cart = Cart.objects.get(user = request.user, active = True)
#             cart.remove_from_cart(id=pk)
#         return redirect('cart')
#     else:
#         return redirect('coursedetails')

def Home(request):
    course = Course.objects.all()
    print(course)
    context ={
        'course':course
    }
    
    return render(request, 'Homepage/home.html',context)
# @login_required

def courses(request):
    return render(request, 'Homepage/courses.html')

def aboutus(request):
    return render(request, 'Homepage/aboutus.html')

def contactus(request): 
    return render(request, 'Homepage/contactus.html')



def doLogin(request):
    if request.method == 'POST':
        user = EmailBackend.authenticate(request, 
                                        username = request.POST.get('email'),
                                        password=request.POST.get('password'),)
        if user!=None:
            login(request,user)                                        
            user_type = user.user_type
            if user_type == '1':
                return redirect("hod_home")
               
            elif user_type == '2':
                return HttpResponse("This is Staff Panel")
            elif user_type =='3':
                return HttpResponse("This is Student Panel")
            else:
                messages.error(request, "Email or Passwrod are Invalid !!")
                return redirect('LOGIN')
        else:
            return redirect('LOGIN')
    else:
            return redirect('LOGIN')


def doLogout(request):
    logout(request)
    return redirect('LOGIN')

from django.shortcuts import render,redirect

# def index(request):
    # return render(request, 'Student/home.html')

def Student_dashboard(request):
    return render(request, 'Student/student-dashboard.html')
def Student_my_subscriptions(request):
    return render(request, 'Student/student-subscription.html')
def Student_my_course(request):
    return render(request, 'Student/student-course-list.html')
def Student_payment_info(request):
    return render(request, 'Student/student-payment-info.html')
def Student_wishlist(request):
    return render(request, 'Student/student-bookmark.html')
def Student_Edit_Profile(request):
    return render(request, 'Student/instructor-edit-profile.html')
def Student_settings(request):
    return render(request, 'Student/instructor-setting.html')
def Student_Delete_Profile(request):
    return render(request, 'Student/instructor-delete-account.html')
def Student_Sign_Out(request):
    return render(request, 'login.html')

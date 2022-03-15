from django.contrib import admin
from .models import Course, CustomUser, Session_Year, Student,Staff
from django.contrib.auth.admin import UserAdmin

# Register your models here.

class UserModel(UserAdmin):
    list_display = ['username', 'user_type']

admin.site.register(CustomUser,UserModel)    
admin.site.register(Course)    
admin.site.register(Session_Year)    
admin.site.register(Student)    
admin.site.register(Staff)    




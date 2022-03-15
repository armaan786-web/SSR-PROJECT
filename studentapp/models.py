from distutils.command.upload import upload
from pyexpat import model
from turtle import update
from django.db import models 
from django.contrib.auth.models import AbstractUser,User


# Create your models here.

class CustomUser(AbstractUser):
    USER = (
        ('1', 'HOD'),
        ('2', 'STAFF'),
        ('3 ', 'STUDENT'),
    )
    user_type = models.CharField(choices=USER, max_length=50)
    profile_pic = models.ImageField(upload_to = 'media/profile_pic')


class Course(models.Model):
    # course_id = models.IntegerField(primary_key=True)
    instructor_name = models.CharField(max_length=100)    
    course_name = models.CharField(max_length=100)    
    course_price = models.IntegerField()    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    profile_course_pic = models.ImageField(upload_to = 'media/profile_course_pic')
    course_title = models.CharField(max_length=500)    
    course_description = models.CharField(max_length=500)    

    def __str__(self):
        return self.course_name

class Session_Year(models.Model):
    session_start = models.CharField(max_length=100)        
    session_end = models.CharField(max_length=100)

    
    def __str__(self):
        return self.session_start + " To " + self.session_end 
    

class Student(models.Model):
    admin = models.OneToOneField(CustomUser,on_delete=models.CASCADE)    
    address = models.TextField()
    gender = models.CharField(max_length=100)
    course_id = models.ForeignKey(Course,on_delete=models.DO_NOTHING)
    session_year_id = models.ForeignKey(Session_Year,on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    profile_img = models.ImageField(upload_to = 'media/student/profile_pic')


    def __str__(self):
        return self.admin.first_name + " " + self.admin.last_name
    

class Staff(models.Model):
    admin =  models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    qualification = models.TextField()
    address = models.TextField()
    gender = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    profile_image = models.ImageField(upload_to = 'media/staff/profile_pic')
 

    def __str__(self):
        return self.admin.username
    
    
# class Cart(models.Model):
#     user = models.ForeignKey(User)
#     active = models.BooleanField(default=True)
#     order_date = models.DateField(null=True)
#     payment_type = models.CharField(max_length=100, null=True)
#     payment_id = models.CharField(max_length=100, null=True)

#     def __unicode__(self): 
#             return "%s" % (self.user)

#     def add_to_cart(self, book_id):
#         book = Book.objects.get(pk=book_id)
#         try:
#             preexisting_order = BookOrder.objects.get(book=book, cart=self)
#             preexisting_order.quantity += 1
#             preexisting_order.save()
#         except BookOrder.DoesNotExist:
#             new_order = BookOrder.objects.create(
#                 book=book,
#                 cart=self,
#                 quantity=1
#                 )
#             new_order.save()

#             def __unicode__(self):
#                 return "%s" % (self.book_id)


# def remove_from_cart(self, book_id):
#         book = Course.objects.get(id=pk)
#         try:
#             preexisting_order = Course.objects.get(course=Course, cart=self)
#             if preexisting_order.quantity > 1:
#                 preexisting_order.quantity -= 1
#                 preexisting_order.save()
#             else:
#                 preexisting_order.delete()
#         except Course.DoesNotExist:
#             pass
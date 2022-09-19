from django.shortcuts import render
from .models import *

# Create your views here.
def Contact(request):
    if request.method=='POST':

        fullname=request.POST['name']
        email=request.POST['email']
        dob=request.POST['date']
        mobile=request.POST['phone']
        gender=request.POST['gender']
        data=Viewers(fullname=fullname,email=email,dob=dob,mobile=mobile,gender=gender)
        data.save()
    return render(request,'contactus.html')

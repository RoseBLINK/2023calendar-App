from django.shortcuts import render

# Create your views here.


from django.shortcuts import render
from django.http import HttpResponse

from .models  import User,Schedule
from django.shortcuts import render


def index(request):
    user_id = User.objects.all()[0].user_id
    user_name = User.objects.all()[0].user_name
    user_email = User.objects.all()[0].user_email


    subject_list = Schedule.objects.all()

    return HttpResponse(user_id+" "+user_name+" "+user_email + " "+subject_list)

def login(request):

    return render(request,"newLogin.html")

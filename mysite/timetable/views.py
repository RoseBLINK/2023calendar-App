from django.shortcuts import render

# Create your views here.


from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .models  import User,Schedule
from django.shortcuts import render


def index(request):
    return HttpResponseRedirect("/timetable/main")

def main(request):
    # if not request.user.is_authenticated:
    #     print("not auth")
    #     return HttpResponseRedirect('/timetable/login')
    # acts = Activity.objects.all().filter(day=day, author_id=request.user.id).order_by('fromTime')
    schedules = Schedule.objects.prefetch_related('subject_name').filter(user_id='test1234')

    # Schedule.objects.prefetch_related('subject')
    print(schedules[0])
    # print(schedules[0].user_id)
    # print(schedules[0].subject_name)

    return render(request,'main.html',{'dayRange' : range(5), 'hourRange' : range(10),'schedules':schedules} )#,{'acts':acts,'day':day}

def login(request):
    return render(request,"newLogin.html")

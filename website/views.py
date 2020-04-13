from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

from meetings.models import Meeting

def welcome(request):
    return render(request, "website/welcome.html",
    {"meetings": Meeting.objects.all()})


def date(request):
    return HttpResponse("This page was server at " + str(datetime.now()))

def about(request):
    return HttpResponse("Hello dudes it is me the enthusiastic Python programmer! Ka-bum-m-m-m")

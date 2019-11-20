from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime


# Create your views here.

def welcome(request):
    return HttpResponse("<h1 style='color:red'>Welcome!</h1>")


def wish(request):
    user = request.GET['user']  # Take value for user parameter
    now = datetime.now()
    if now.hour < 12:
        msg = "Good Morning"
    elif now.hour < 17:
        msg = "Good Afternoon"
    else:
        msg = "Good Evening"

    return HttpResponse(f"<h1>{msg} {user}</h1>")
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
import requests


# Create your views here.

def welcome(request):
    return HttpResponse("<h1 style='color:red'>Welcome!</h1>")


def greet(request):
    now = datetime.now().strftime("%d-%m-%y %H:%M:%S")
    return render(request, 'greet.html', {'now': str(now)})


def wish(request):
    if 'user' in request.GET:
        user = request.GET['user']  # Take value for user parameter
    else:
        user = "Guest"

    now = datetime.now()
    if now.hour < 12:
        msg = "Good Morning"
    elif now.hour < 17:
        msg = "Good Afternoon"
    else:
        msg = "Good Evening"

    return HttpResponse(f"<h1>{msg} {user}</h1>")


def list_countries(request):
    resp = requests.get("https://restcountries.eu/rest/v2/all")
    countries = resp.json()
    countries = sorted(countries,
                       key=lambda c: c['population'],
                       reverse=True)[:20]
    return render(request, 'list_countries.html', {'countries': countries})


def ajax_demo(request):
    return render(request, 'ajax_demo.html')


def send_datetime(request):
    return HttpResponse(str(datetime.now()))

from django.urls import path
from . import views

urlpatterns = [
    path('welcome/', views.welcome),
    path('wish/', views.wish),
    path('greet/',views.greet),
    path('countries/', views.list_countries),

]

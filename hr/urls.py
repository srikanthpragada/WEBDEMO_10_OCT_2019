from django.urls import path
from . import views, employee_views

urlpatterns = [
    path('welcome/', views.welcome),
    path('wish/', views.wish),
    path('greet/',views.greet),
    path('countries/', views.list_countries),
    path('employees/', employee_views.list_employees),
    path('add_employee/', employee_views.add_employee),
    path('add_employee2/', employee_views.add_employee_with_form),
    path('update_salary/', employee_views.update_salary),

]

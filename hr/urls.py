from django.urls import path
from . import views, employee_views, author_views

urlpatterns = [
    path('welcome/', views.welcome),
    path('wish/', views.wish),
    path('greet/',views.greet),
    path('countries/', views.list_countries),
    path('employees/', employee_views.list_employees),
    path('add_employee/', employee_views.add_employee),
    path('add_employee2/', employee_views.add_employee_with_form),
    path('update_salary/', employee_views.update_salary),
    path('author/home/', author_views.author_home),
    path('author/list/', author_views.author_list),
    path('author/delete/<int:id>', author_views.author_delete),
    path('author/add/', author_views.author_add),
    path('author/edit/<int:id>', author_views.author_edit),
]

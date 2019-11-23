from django.shortcuts import render, redirect
import sqlite3
from .forms import UpdateSalaryForm, AddEmployeeForm


def list_employees(request):
    con = sqlite3.connect(r"e:\classroom\python\oct10\hr.db")
    cur = con.cursor()
    cur.execute("select * from employees")

    employees = cur.fetchall()
    con.close()

    return render(request, "list_employees.html", {'employees': employees})


def add_employee(request):
    if request.method == "POST":
        # take data from parameters and insert a row in Employees table
        empname = request.POST['empname']
        job = request.POST['job']
        salary = request.POST['salary']
        # Connect to DB
        con = sqlite3.connect(r"e:\classroom\python\oct10\hr.db")
        cur = con.cursor()
        cur.execute("insert into employees(empname,job,salary) values(?,?,?)",
                    (empname, job, salary))
        con.commit()
        return redirect("/hr/employees")
    else:  # GET request
        return render(request, 'add_employee.html')


def update_salary(request):
    if request.method == "GET":
        f = UpdateSalaryForm()
        return render(request, 'update_salary.html', {'form': f})
    else:  # POST
        f = UpdateSalaryForm(request.POST)
        if f.is_valid():
            id = f.cleaned_data['empid']
            salary = f.cleaned_data['newsalary']
            con = sqlite3.connect(r"e:\classroom\python\oct10\hr.db")
            cur = con.cursor()
            cur.execute("update employees set salary = ? where empid = ?",
                        (salary, id))
            if cur.rowcount == 1:
                con.commit()
                return render(request, 'update_salary.html',
                              {'form': f, 'msg': "Updated Successfully"})
            else:
                return render(request, 'update_salary.html',
                              {'form': f, 'msg': "Sorry! Employee id not found!"})
        else:
            return render(request, 'update_salary.html', {'form': f})


def add_employee_with_form(request):
    if request.method == "POST":
        # take data from parameters and insert a row in Employees table
        f = AddEmployeeForm(request.POST)
        if f.is_valid():
            empname = f.cleaned_data['name']
            job = f.cleaned_data['job']
            salary = f.cleaned_data['salary']
            # Connect to DB
            con = sqlite3.connect(r"e:\classroom\python\oct10\hr.db")
            cur = con.cursor()
            cur.execute("insert into employees(empname,job,salary) values(?,?,?)",
                    (empname, job, salary))
            con.commit()
            return redirect("/hr/employees")
        else:
            return render(request, 'add_employee_with_form.html', {'form': f})
    else:  # GET request
        f = AddEmployeeForm()
        return render(request, 'add_employee_with_form.html', {'form' : f})
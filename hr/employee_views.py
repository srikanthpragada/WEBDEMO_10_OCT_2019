from django.shortcuts import render, redirect
import sqlite3


def list_employees(request):
    con = sqlite3.connect(r"e:\classroom\python\oct10\hr.db")
    cur = con.cursor()
    cur.execute("select * from employees")

    employees = cur.fetchall()
    con.close()

    return render(request, "list_employees.html", {'employees': employees})


def add_employee(request):
    if 'empname' in request.GET:
        # take data from parameters and insert a row in Employees table
        empname = request.GET['empname']
        job = request.GET['job']
        salary = request.GET['salary']
        # Connect to DB
        con = sqlite3.connect(r"e:\classroom\python\oct10\hr.db")
        cur = con.cursor()
        cur.execute("insert into employees(empname,job,salary) values(?,?,?)",
                    (empname,job,salary))
        con.commit()
        return redirect("/hr/employees")
    else:
        return render(request, 'add_employee.html')

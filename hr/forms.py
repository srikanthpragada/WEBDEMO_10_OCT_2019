import django.forms as forms


class UpdateSalaryForm(forms.Form):
    empid = forms.IntegerField(label="Employee Id")
    newsalary = forms.IntegerField(label="New Salary")


class AddEmployeeForm(forms.Form):
    name = forms.CharField(label="Fullname", max_length=50, min_length=5)
    job = forms.CharField(label="Job", required=False, max_length=50)
    salary = forms.IntegerField(label="Salary", min_value=10000)

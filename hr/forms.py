import django.forms as forms


class UpdateSalaryForm(forms.Form):
    empid = forms.IntegerField(label="Employee Id")
    newsalary = forms.IntegerField(label="New Salary")
